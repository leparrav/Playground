export const a = async () => 1;
export const b = new Promise((resolve) => resolve(2));
export const c = new Promise((_, reject) => reject(3));
export const d = new Promise((resolve, reject) => {
  const random = (input1, input2) => (Math.random() > 0.5 ? input1 : input2);
  const action = random(resolve, reject);
  action(3);
});

export function test(payload, equal = 6) {
  const result =
    payload === equal
      ? "Test is successful"
      : `Test is failed, received: ${payload}`;
  console.log(result);
  document.getElementById("app").innerHTML = result;
  return result;
}

export class Library {
  constructor() {
    // delay up to 5 secs
    // async () => number; - always success = 1
    this.a = a;
    // delay up to 5 secs
    // Promise<number>; - always success = 2
    this.b = b;
    // delay up to 5 secs
    // Promise<number, number>; - random success/fail = 3
    this.c = c;
    // !IGNORE! delay up to 5 secs
    // Promise<number, number> // random resolve/reject 3
    this.dd = d;
  }
}

export const testFunc = (solution) => {
  solution()
    .then((sum) => {
      test(sum);
    })
    .catch((err) => {
      test(err);
      // console.log("Test is failed");
      console.error(err);
    });
};
