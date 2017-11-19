#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import smtplib
from email import encoders as Encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate, COMMASPACE
if sys.version_info < (3, 0):
    from sgmllib import SGMLParser
else:
    from html.parser import HTMLParser as SGMLParser


class ConnectionError(Exception):
    pass


class AuthError(Exception):
    pass


class SendError(Exception):
    pass


class Mail(object):
    """
    Email sending.
    """
    # Error codes
    __ERROR_SMTP_CONNECTION = 1000
    __ERROR_SMTP_AUTHENTICATION = 1001

    def __init__(self, opts={}):
        """
        Constructor

        @param server: smtp server address (default: localhost)
        @param port: connection port (default: 25)
        @param user: smtp username (default: None)
        @param password: smtp password (default: None)
        @param encryption: encryption method (values: None, 'starttls'; default: None)
        @param delivery_notification: send delivery notification (values: True, False; default: False)
        @param return_receipt: send return receipt (values: True, False; default: False)
        """
        self.opts = opts
        self.__smtp = {'server': self.opts.get('server', 'localhost'),
                       'port': self.opts.get('port', 25),
                       'user': self.opts.get('user', None),
                       'password': self.opts.get('password', None),
                       'encryption': self.opts.get('encryption', None)}
        self.__notify = {'delivery_notification': self.opts.get('delivery_notification', False),
                         'return_receipt': self.opts.get('return_receipt', False)}
        self.__attacments = None
        self.__images = None

    def set_smtp(self, server, port=25, user=None, password=None, encryption=None):
        """
        Set/change stmp server values.

        @param server: smtp server address
        @param port: connection port (default: 25)
        @param user: smtp username (default: None)
        @param password: smtp password (default: None)
        @param encryption: encryption method (values: None, 'starttls'; default: None)
        """
        self.__smtp['server'] = server
        self.__smtp['port'] = port
        self.__smtp['user'] = user
        self.__smtp['password'] = password
        self.__smtp['encryption'] = encryption

    def set_notify(self, delivery_notification=False, return_receipt=False):
        """
        Set/change notification options: 'delivery notification' and 'return receipt'

        @param delivery_notification: send delivery notification (values: True, False; default: False)
        @param return_receipt: send return receipt (values: True, False; default: False)
        """
        self.__notify['delivery_notification'] = delivery_notification
        self.__notify['return_receipt'] = return_receipt

    def set_attachments(self, files):
        """
        Files to be attached

        @param files: list of filenames (with path) to be attached
        """
        self.__attacments = files

    def set_images(self, images):
        self.__images = images

    def get_parameters(self):
        """
        Return current configuration parameters

        @return: Dictionary with all configuration parameters
        """
        return {'smtp': self.__smtp,
                'notify': self.__notify,
                'attacments': self.__attacments}

    def __str__(self):
        """
        Return current configuration parameters as string.

        @return: String with all configuration parameters
        """
        return repr(self.get_parameters())

    def __send_mail(self, send_from, send_to, send_cc, send_bcc, subject, message, message_type, img=None):
        """
        Internal method that send mail with current configuration parameters (smtp, notification and attachments)

        @param send_from: sender (e-mail address)
        @param send_to: List of recipients (e-mail addresses)
        @param send_cc: List of recipients (email addresses) as carbon copy
        @param send_bcc: List of recipients (email addresses) as blind carbon copy
        @param subject: Message subject
        @param message: Message body
        @param message_type: Message type (values: 'text' o 'html')
        @return: Sending result (True or False)
        """
        # Message data
        msg = MIMEMultipart('related')
        # sender and recipients
        msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)

        # CC recipients
        if send_cc:
            msg['Cc'] = COMMASPACE.join(send_cc)

        # BCC recipients
        if send_bcc:
            msg['Bcc'] = COMMASPACE.join(send_bcc)

        # sending date (current date)
        msg['Date'] = formatdate(localtime=True)

        # message body
        msg['Subject'] = subject

        # delivery notification address (sender)
        if self.__notify['delivery_notification']:
            msg['Disposition-Notification-To'] = send_from

        # return receipt address (sender)
        if self.__notify['return_receipt']:
            msg['Return-Receipt-To'] = send_from

        # Message type
        if message_type == 'html':
            # message, images = self.parse_html(message)
            msg.attach(MIMEText(message, 'html', 'utf-8'))
        #     # if type(images) == type({}) and images:
        #     if isinstance(images, dict) and images:
        #         for name, img in images.iteritems():
        #             image = MIMEImage(img[1])
        #             image.add_header("Content-Disposition", 'inline; filename="%s"' % name)
        #             image.add_header('Content-ID', '<%s>' % img[0])
        #             msg.attach(image)
        else:
            # plain not text
            msg.attach(MIMEText(message, 'plain', 'utf-8'))

        # --- Message with attachments ---
        if self.__attacments is not None:
            # Attachemnt files
            for f in self.__attacments:
                part = MIMEBase('application', "octet-stream")
                try:
                    part.set_payload(open(f, "rb").read())
                    Encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
                    msg.attach(part)
                except:
                    pass

        if self.__images is not None:
            for name, img in self.__images.items():
                with open(img, 'rb') as f:
                    image = MIMEImage(f.read())
                    image.add_header("Content-Disposition", 'inline; filename="%s"' % name)
                    image.add_header('Content-ID', '<%s>' % name)
                    msg.attach(image)

        # open STMP server connection
        try:
            smtp = smtplib.SMTP(self.__smtp['server'], self.__smtp['port'])
        except smtplib.socket.gaierror:
            raise ConnectionError("Server connection error (%s)" % (self.__smtp['server']))

        # active encryption
        if (self.__smtp['encryption']) and (self.__smtp['encryption'] == "starttls"):
            smtp.ehlo_or_helo_if_needed()
            smtp.starttls()

        # execute STMP server login
        if self.__smtp['user']:
            smtp.ehlo_or_helo_if_needed()
            try:
                smtp.login(self.__smtp['user'], self.__smtp['password'])
            except smtplib.SMTPAuthenticationError:
                smtp.close()
                raise AuthError("Invalid username or password (%s)" % (self.__smtp['user']))

        # send e-mail
        try:
            if send_cc:
                send_to += send_cc
            if send_bcc:
                send_to += send_bcc

            smtp.sendmail(send_from, send_to, msg.as_string())
            return True
        except Exception as errormsg:
            raise SendError("Unable to send e-mail: %s" % (errormsg))
        except smtp.socket.timeout:
            raise ConnectionError("Unable to send e-mail: timeout")
        finally:
            # close SMTP server connection
            smtp.close()

    def send_html(self, subject='', message='', attach_file='', images={}):
        """
        Send HTML e-mail.

        @param send_from: sender (e-mail address)
        @param send_to: List of recipients (comma separated e-mail addresses)
        @param subject: Message subject
        @param message: Message body
        @param send_cc: List of CC recipients (comma separated e-mail addresses)
        @param send_bcc: List of BCC recipients (comma separated e-mail addresses)
        @return: Sending result (True or False)
        """
        # Se presenti i destinatari, ne crea una lista

        send_from = self.opts.get('send_from', None)
        send_to = self.opts.get('send_to', None)
        send_cc = self.opts.get('send_cc', None)
        send_bcc = self.opts.get('send_bcc', None)
        if not all([send_to, send_from]):
            return self.opts, False, send_to
        if send_to:
            send_to = send_to.split(',')
        if send_cc:
            send_cc = send_cc.split(',')
        if send_bcc:
            send_bcc = send_bcc.split(',')
        if attach_file:
            if sys.version_info < (3, 0):
                if isinstance(attach_file, basestring):
                    self.set_attachments([attach_file])
                else:
                    self.set_attachments(attach_file)
            else:
                if isinstance(attach_file, str):
                    self.set_attachments([attach_file])
                else:
                    self.set_attachments(attach_file)

        if images and isinstance(images, dict):
            self.set_images(images)

        # Invio dell' email
        return self.__send_mail(send_from, send_to, send_cc, send_bcc, subject, message, 'html')
