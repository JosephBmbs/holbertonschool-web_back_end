export default class HolbertonCourse {
	constructor(name, length, students) {
    if (typeof name !== 'string') {
  	throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
  	throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students) || students.some(student => typeof student !== 'string')) {
  	throw new TypeError('Students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  /* getter the name */
  get name() {
    return this._name;
  }

  /* setter the name */
  set name(value) {
    if (typeof value !== 'string') {
  	throw new TypeError('Name must be a string');
    }
    this._name = value;
  }
  
  /* getter the length */
  get length() {
    return this._length;
  }
  
  /* setter the length */
  set length(value) {
    if (typeof value !== 'number') {
  	throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  /* getter the students */
  get students() {
    return this._students;
  }

  /* setter the students */
  set students(value) {
    if (!Array.isArray(value) || value.some(student => typeof student !== 'string')) {
  	throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
