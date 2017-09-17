package com.matrix.momgodb.repo;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import com.matrix.momgodb.data.User;

@Repository("userRepo")
public interface UserRepo extends MongoRepository<User,String> {

	
}
