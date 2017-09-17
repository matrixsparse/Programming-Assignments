package com.matrix.momgodb.momgodb_example;

import java.util.List;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import com.matrix.momgodb.data.User;
import com.matrix.momgodb.service.UserService;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = { "classpath:spring-context.xml" })
public class UserTest {

	@Autowired
	UserService userService;

	@Test
	public void getUser() {
		// 查询
		// List<User> users = userService.getList();
		// for (User user : users) {
		// System.out.println(user.getId() + " " + user.getName() + " " +
		// user.getAddress());
		// }

		// 插入
		// userService.insertUser();

		// 更新
		// userService.updateUser(1);

		// 删除
		// userService.removeUser(1);
	}
}
