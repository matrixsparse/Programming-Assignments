# Overview

Training and evaluating deep neural networks is a computationally intensive task. For modestly sized problems and datasets it may be possible to train your network on the CPU in your local machine, but it could take anywhere from 15 minutes to several hours depending on the number of epochs, the size of the neural networks, and other factors. A faster alternative is to train on a GPU (Graphics Processing Unit), which is a type of processor that supports greater parallelism.

If you do not already have a computer with a built-in NVIDIA GPU, we suggest you use an Amazon EC2 instance. There are many cloud service providers that offer equivalent functionality, but EC2 is a reasonable default that is available to most students. In the next few sections, we'll go over the steps from nothing to running a neural network on an Amazon server.

Note: Please skip this section if you are planning to use your own GPU or CPU (or otherwise not planning to use Amazon EC2).
Note: We provide AWS credits to DLND students, but currently not to MLND students.
