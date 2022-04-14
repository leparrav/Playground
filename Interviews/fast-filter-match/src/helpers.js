export function test(input, exmaple = [0, 2, 4]) {
  if (!input.length) return `Input: ${input} is not equal to ${exmaple}`;
  let result = true;
  for (let i; i < input.length; i++) {
    if (input[i] !== exmaple[i]) {
      result = false;
      break;
    }
  }
  if (result) {
    return "success";
  } else {
    return `Input: ${input} is not equal to ${exmaple}`;
  }
}
