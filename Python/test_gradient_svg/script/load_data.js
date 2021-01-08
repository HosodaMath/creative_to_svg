let img_load1 = async () => {
  const response1 = await fetch("./svg/test1_linear_gradient1.svg");
  const code1 = await response1.text();
  document.getElementById("container1").innerHTML = code1;
}

let img_load2 = async () => {
  const response2 = await fetch("./svg/test2_linear_gradient1.svg");
  const code2 = await response2.text();
  document.getElementById("container2").innerHTML = code2;
}

let main = () => {
  img_load1();
  img_load2();
}

main();