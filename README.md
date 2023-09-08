# README
## Introduction
This README file provides information about the project and its components. The project is aimed at automating the database management process and streamlining the storage system for different levels of stores.

Technology Stack
The following technologies have been used in the project:

Flask: A web framework for Python.a
OpenCV: A computer vision library.
Python: A high-level programming language.
MySQL: A relational database management system.
Pyzbar: A library for reading barcodes.#
Bcrypt: A library for securely hashing passwords.
## Usage
The project is intended to be used in database management and in all levels of stores. It aims to simplify the process of managing information and ensure the accuracy of stored data.

##Installation
### First you have to create 2 databases:
1. ims 
2. ims_users
### In ims_users you have to create a table user, with two fields:
1. userid
2. password

### Commands

#### create database ims;
#### create database ims_users;
#### use ims_users;
#### create table user(userid varchar (100), password varchar(400));

## Authors
The project has been developed by the following individuals:

Gundeep Singh
Ekamdeep Singh Mangat
Chandanbir Singh
## Acknowledgements
The authors would like to acknowledge the contributions of StackOverflow in helping them resolve various technical issues faced during the development of the project.

## Summary
The purpose of our application seems to be an Inventory Management System (IMS) that allows users to sign up, log in, and manage their inventory by adding products with serial numbers, product names, and prices. The application uses the following libraries:

- Flask for web development
- pyzbar for barcode decoding
- OpenCV for image processing
- NumPy for numerical computation
- mysql-connector for connecting to a MySQL database
- bcrypt for password hashing

Our code has multiple routes for handling different pages in the application such as the home page, the signup page, the login page, and the product addition page. When a new user signs up, the information is stored in a MySQL database with a hashed password. When a user logs in, their username and password are verified against the stored data in the database. If the login is successful, the user is redirected to the inventory page where they can add a new product. If the product has a barcode, the barcode is read using pyzbar and decoded to get the serial number. The product information is then inserted into the user's inventory table in the MySQL database.
