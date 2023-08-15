#!usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // Create an empty object if w or h is not valid
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

// Example usage
const rectangle1 = new Rectangle(5, 3);
rectangle1.print();

const rectangle2 = new Rectangle(0, 4); // This will create an empty object
rectangle2.print();
