package com.matrix.momgodb.momgodb_example;

import java.util.Set;

import org.junit.Test;

import com.mongodb.DB;
import com.mongodb.Mongo;

public class TestMongoDB {

	@Test
	public void testMongodb() {
		try {
			Mongo mongo = new Mongo("115.28.240.96", 27017);
			DB db = mongo.getDB("test");

			Set<String> collections = db.getCollectionNames();

			for (String name : collections) {
				System.out.println("collection=" + name);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
