interface ISome1 {
  a: number;
  b: number;
  c: number;
}

// extend ISome2 from ISome1 except 'c'
interface ISome2 extends Exclude<{c: number}, ISome1 > {
  d: number;
}

// What the diff in JS after transpiling
type Union = "asd" | "zxc" | "wqe";

enum Enum1 {
  "asd", // asd = "asd",
  "zxc", // zxc = "zxc",
  "wqe" // wqe = "wqe",
}

enum Enum2 {
  asd = "asd",
  zxc = "zxc",
  wqe = "wqe"
}

// What the diff in JS after transpiling
interface ISomeClass {
  a: number;
  b: number;
  c: number;
}

class SomeClass1 implements ISomeClass {
  a = 1;
  b = 2;
  c = 3;
}

abstract class AbstractSomeClass {
  abstract a: number;
  abstract b: number;
  abstract c: number;
}

class SomeClass2 extends AbstractSomeClass {
  a = 1;
  b = 2;
  c = 3;
}
