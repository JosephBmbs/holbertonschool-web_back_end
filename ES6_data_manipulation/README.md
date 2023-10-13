<div align="center">
  <h1>ES6 Data Manipulation</h1>
  <img src="https://i.stack.imgur.com/INdOQ.gif" alt="ES6 Data Manipulation">
</div>

## Overview

This project explores the fundamentals of ES6 data manipulation, focusing on using array methods such as `map`, `filter`, and `reduce`. It also delves into typed arrays and introduces data structures like Set, Map, and WeakMap. By the end of this project, you will have a strong grasp of data manipulation techniques in ES6.

## Author

- **Youssef Saad**
- *Software Engineering student at Holberton School*

## Learning Objectives

Upon completing this project, you will be able to:

- Understand what Promises are and why they are essential in asynchronous programming.
- Utilize the `then`, `resolve`, and `catch` methods to handle Promise states.
- Master the `every` method for better control and management of Promise objects.
- Implement error handling techniques using `Throw` and `Try` to ensure robust code.
- Learn about the `await` operator and its significance in modern JavaScript.
- Create and work with asynchronous functions to manage complex tasks efficiently.

## Requirements

- The project should be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x.
- Supported editors: vi, vim, emacs, Visual Studio Code.
- All code files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- All code files should use the `.js` extension.
- Code will be tested using Jest with the command `npm run test`.
- Code will be verified against lint using ESLint.
- All functions must be exported as specified.

## Setup

### Install NodeJS 12.11.x

To set up NodeJS 12.11.x, follow these steps:

1. In your home directory, run the following commands:

   ```bash
   curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
   sudo bash nodesource_setup.sh
   sudo apt install nodejs -y
   ```
2. Verify the NodeJS and npm versions:

	```bash
nodejs -v
npm -v
Install Jest, Babel, and ESLint
    ``` 
In your project directory, install the necessary dependencies:

3. Install Jest:
```bash
npm install --save-dev jest
```
4. Install Babel:
```bash
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
```
5. Install ESLint:
```bash
npm install --save-dev eslint
```

## Files

package.json
babel.config.js
utils.js - Use when you get to tasks requiring uploadPhoto and createUser.
.eslintrc.js

## Response Data Format

### uploadPhoto returns a response in the following format:
json
```bash
{
  "status": 200,
  "body": "photo-profile-1"
}
```
### createUser returns a response in the following format:
json
```bash
{
  "firstName": "Guillaume",
  "lastName": "Salva"
}
```
