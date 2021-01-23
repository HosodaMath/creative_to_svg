let img_load1 = async () => {
  const response1 = await fetch("./svg/test1_linear_gradient_pattern1.svg");
  const code1 = await response1.text();
  document.getElementById("container1").innerHTML = code1;
}

let img_load2 = async () => {
  const response2 = await fetch("./svg/test1_linear_gradient_pattern2.svg");
  const code2 = await response2.text();
  document.getElementById("container2").innerHTML = code2;
}

let img_load3 = async () => {
  const response3 = await fetch("./svg/test1_linear_gradient_pattern3.svg");
  const code3 = await response3.text();
  document.getElementById("container3").innerHTML = code3;
}

let main = () => {
  img_load1();
  img_load2();
  img_load3();
}

main();
