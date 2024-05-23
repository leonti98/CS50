const get = (query) => document.querySelector(query);
const wait = (s) => new Promise((r) => setTimeout(r, s * 1000));

const display = get('.timer .display');
const progress = get('.timer .progress');

const INIT_TIME = 5;
let timeRemaining = INIT_TIME;

(async () => {
  while (true) {
    while (timeRemaining > 0) {
      timeRemaining--;
      display.innerText = `${timeRemaining}s`;
      const newProgress = timeRemaining / INIT_TIME;
      progress.style.setProperty('--progress', newProgress);
      await wait(1);
    }
    timeRemaining = INIT_TIME;
    display.innerText = `${timeRemaining}s`;
    progress.style.setProperty('--progress', 1);
  }
})();
