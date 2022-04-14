const { testFunc, Library } = require("./helpers");

// each method has delay up to 5 seconds!!!
// interface Library {
//   a: async () => ...<number> // return 1
//   b: Promise<number> // resolve 2
//   c: Promise<never, number> // reject 3
//   !IGNORE! d: Promise<number, number> // random resolve/reject 3
// }
const library = new Library();

const solution = async () => {
  let sum = 0; // 1 + 2 + 3 = 6;
  // TODO: start here!
  // ...
  const n1 = new Promise(async (resolve, reject) => resolve(await library.a()) );
  const n2 = library.b;
  const n3 = library.c;

  const [v1, v2, v3] = await Promise.allSettled([n1, n2, n3]);
  sum = v1.value + v2.value + v3.reason;
  // end
  return sum;
};

testFunc(solution);
