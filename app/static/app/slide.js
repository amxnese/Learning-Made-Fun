let next = document.querySelector(".next");
let prev = document.querySelector(".prev");
let slider = document.querySelector(".slider");
next.addEventListener('click', function() {
  let slides = document.querySelectorAll('.slide');
  let slidesArr = Array.from(slides);
  let active = slidesArr.findIndex(slide => slide.classList.contains('active'))
  if(active+1 < slides.length){
    slides[active].classList.remove('active')
    slides[active+1].classList.add('active')
    console.log(active);
    slider.style.transform = `translateX(${-700*(active+1)}px)`;
  }
})
prev.addEventListener('click', function() {
  let slides = document.querySelectorAll('.slide');
  let slidesArr = Array.from(slides);
  let active = slidesArr.findIndex(slide => slide.classList.contains('active'))
  if(active > 0){
    slides[active].classList.remove('active')
    slides[active-1].classList.add('active')
    console.log(active);
    slider.style.transform = `translateX(${-700*(active-1)}px)`;
  }
})