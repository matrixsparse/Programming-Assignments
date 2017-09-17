package com.matrix.momgodb.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.matrix.momgodb.data.User;
import com.matrix.momgodb.repo.UserRepo;
import com.matrix.momgodb.service.UserService;

@Service("userService")
public class UserServiceImpl implements UserService {

	@Autowired
	UserRepo userRepo;

	/**
	 * 
	 */

	public List<User> getList() {
		return userRepo.findAll();
	}

	public void updateUser(int id) {
		User user = new User();
		user.setId(id);
		user.setName("888888888888888888");
		user.setAddress("ddddddddddddddddddddddddddddd");
		User reuser = userRepo.save(user);
		System.out.println(reuser.getName());
	}

	public void insertUser() {
		User user = new User();
		for (int i = 1; i <= 50; i++) {
			user.setId(i);
			user.setName("Matrix " + i);
			user.setAddress("shenzhen " + i);

			User users = userRepo.insert(user);
			System.out.println(users.getId());
		}
	}

	public void removeUser(int id) {
		User user = new User();
		user.setId(id);
		userRepo.delete(user);
	}

}
