'use strict';
const track = document.querySelector('#badge-track');
const previous = document.querySelector('#previous');
const next = document.querySelector('#next');
const cards = [...track.querySelectorAll('.badge-card')];
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
document.querySelector('.carousel-controls').hidden = false;
function updateControls() {
  const max = track.scrollWidth - track.clientWidth;
  previous.disabled = track.scrollLeft <= 2;
  next.disabled = track.scrollLeft >= max - 2;
  const step = cards[0].getBoundingClientRect().width + 18;
  const first = Math.min(cards.length, Math.round(track.scrollLeft / step) + 1);
  document.querySelector('#position').textContent = `Badge ${first} of ${cards.length}`;
}
function move(direction) {
  const step = cards[0].getBoundingClientRect().width + 18;
  track.scrollBy({ left: direction * step, behavior: reducedMotion.matches ? 'instant' : 'smooth' });
}
previous.addEventListener('click', () => move(-1));
next.addEventListener('click', () => move(1));
track.addEventListener('keydown', event => {
  if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
    event.preventDefault();
    move(event.key === 'ArrowRight' ? 1 : -1);
  }
});
let timer;
track.addEventListener('scroll', () => { clearTimeout(timer); timer = setTimeout(updateControls, 100); }, { passive: true });
window.addEventListener('resize', updateControls);
document.querySelector('#year').textContent = new Date().getFullYear();
document.querySelectorAll('.badge-art img').forEach(img => {
  const showFallback = () => {
    const label = document.createElement('span');
    label.className = 'fallback';
    label.textContent = img.alt;
    img.replaceWith(label);
  };
  img.addEventListener('error', showFallback, { once: true });
  if (img.complete && img.naturalWidth === 0) showFallback();
});
updateControls();
