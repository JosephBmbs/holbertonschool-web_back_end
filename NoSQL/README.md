<div align="center">
  <h1>NoSQL</h1>
  <img src="https://cdn3.vectorstock.com/i/1000x1000/85/52/nosql-non-relational-database-concept-vector-10208552.jpg" alt="NoSQL Logo">
</div>

## Table of Contents

- [Project Description](#project-description)
- [Team](#team)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [MongoDB Installation](#mongodb-installation)
- [Python Scripts](#python-scripts)
- [More Info](#more-info)

---

## Project Description

Welcome to the NoSQL project! This project provides an introduction to NoSQL databases, focusing on MongoDB, and covers various aspects of working with NoSQL databases and Python. It is designed to help you understand the fundamentals of NoSQL, document storage, and how to interact with MongoDB.

**Project Leads**:
- Emmanuel Turlay, Staff Software Engineer at Cruise
- Guillaume, CTO at Holberton School

**Project Weight**: 1

**Score**: Your score will be updated as you progress.

### Resources

For this project, you are encouraged to read or watch the following resources:

- [NoSQL Databases Explained](https://intranet.hbtn.io/rltoken/0HR2bZ3XFJzkttuEVF5Rug)
- [What is NoSQL?](https://intranet.hbtn.io/rltoken/JGxz6PJsAN9cjBBT_WVCAg)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://intranet.hbtn.io/rltoken/PkdXgnfXUfJIk5iqf9Wp4A)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://intranet.hbtn.io/rltoken/y6ncfHy0Hn7uqaIyitWQRg)
- [Aggregation](https://intranet.hbtn.io/rltoken/sIORcQADQT2Wf2opdMu30Q)
- [Introduction to MongoDB and Python]https://intranet.hbtn.io/rltoken/BLt93wwWTkVQWVlSDerI1g)
- [mongo Shell Methods](https://intranet.hbtn.io/rltoken/q-RfEFpmN-fGiX-SvmQjHA)
- [The mongo Shell](https://intranet.hbtn.io/rltoken/fmrWM3wzfC2d2-WHqzzPBQ)

### Learning Objectives

By the end of this project, we should be able to explain the following concepts without relying on external sources:

**General**:
- What NoSQL means
- The difference between SQL and NoSQL
- ACID (Atomicity, Consistency, Isolation, Durability)
- Document storage in NoSQL
- Types of NoSQL databases
- Benefits of using a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

---

## Team

This project can be completed individually or as a team. Feel free to collaborate if you wish!

**Youssef Saad**
---

## Requirements

**MongoDB Command File**:
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: `// my comment`
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

**Python Scripts**:
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

---

## Getting Started

To get started with this project, follow the installation instructions and guidelines below.

---

## MongoDB Installation

Follow these steps to install MongoDB 4.2 on Ubuntu 18.04:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
$ mongo --version
$ pip3 install pymongo
```

## More Info
For additional information and resources, please refer to the official MongoDB installation guide and other helpful documentation.
Official MongoDB Installation Guide

## License

This project is licensed under the MIT License.
