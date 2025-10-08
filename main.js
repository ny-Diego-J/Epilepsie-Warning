function download() {}

function hover() {
  let download = document.querySelector("img");
  const windowWidth = window.innerWidth;
  const windowHeight = window.innerHeight;
  const imgWidth = download.offsetWidth;
  const imgHeight = download.offsetHeight;

  let randx = Math.floor(Math.random() * windowWidth);
  let randy = Math.floor(Math.random() * windowHeight);

  let randomy = Math.floor(Math.random() * 1000);
  let randomx = Math.floor(Math.random() * 1000);

  download.style.width = randomx + "px";
  download.style.height = randomy + "px";
  if (randx + imgWidth >= windowWidth) {
    randx = windowWidth - imgWidth;
  } else if (randx < 0) {
    randx = 0;
  } else if (randy + imgHeight >= windowHeight) {
    randy = windowHeight - imgHeight;
  } else if (randy < 0) {
    randy = 0;
  } else if (randx == download.style.left) {
    randx = randx + 100;
  } else if (randy == download.style.top) {
    randy = randy + 100;
  }

  download.style.left = randx + "px";
  download.style.top = randy + "px";
  download.style.cursor = "pointer";
  download.style.transitionDuration = "0.5s";
}
