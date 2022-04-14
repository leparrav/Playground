const { test } = require("./helpers");

// aN = 1000, uniq, not sorted
const aAr = [0, 1, 2, 3, 4, 5];
// bN = 1000, uniq, not sorted
const bAr = [0, 2, 4, 6, 8, 10];

// find all common (intersction) elements
// depending on JS engine performance
// & complexity of algorithms
function intersection(a, b) {
  // solutiuon ...

  // Simple solution O(n*n) = O(n2)
  // const cAr = a.filter((item) => b.includes(item));

  // Using set O(n+n) = O(n)
  const setA = new Set(a);
  const setB = new Set(b);
  const dAr = [...setA.values()].filter((val) => setB.has(val));
  
  return dAr;
}

const cAr = intersection(aAr, bAr) || [];
console.log(cAr); // [0, 2, 4]
test(cAr, [0, 2, 4]);
