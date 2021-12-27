// link : https://www.codewars.com/kata/56a1c63f3bc6827e13000006

function smaller(arr) {
  smaller_array = []
  // for(let i = 0; i < arr.length; i++) {
  //   smaller_array.push(0);
  //   for(let j = i; j < arr.length; j++) {
  //     if(arr[i] > arr[j]) 
  //       smaller_array[i] += 1;
  //   }
  // }
  for(let i = 0; i < arr.length; i++) { 
    smaller_array.push([arr[i], i + 1])
  }
  smaller_array.sort(function(a, b) {a[0] - b[0]})
  return smaller_array;
}

console.log(smaller([1, 4, 5, 2, 6]))

  