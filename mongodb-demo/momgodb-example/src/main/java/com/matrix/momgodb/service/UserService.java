package com.matrix.momgodb.service;

import java.util.List;

import com.matrix.momgodb.data.User;

public interface UserService {

	public List<User> getList();
	public void updateUser(int id);
	public void insertUser();
	public void removeUser(int id);
}
