(function () {
  a();
  function a() {
    console.log("a");
  }

  b();
  var b = function () {
    console.log("b");
  };

  c();
  const c = function () {
    console.log("c");
  };

  // d();
  // if (true) {
  //   function d() {
  //     console.log("d");
  //   }
  // }
})();
// (function () {
//  a();
//  function a() {
//    console.log("a");
//  }
//
//  console.log(b);
//  var b = 'b';
//
//  console.log(c);
//  c = "c";
// })
