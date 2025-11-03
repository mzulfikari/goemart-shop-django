function formatPriceInToman(element) {
  let rawPrice = parseFloat(element.innerText);
  let formatter = new Intl.NumberFormat("fa-IR");
  let formattedPrice = formatter.format(rawPrice);
  element.innerText = `${formattedPrice} تومان`;
}

document.addEventListener("DOMContentLoaded", function () {
  let priceElements = document.querySelectorAll(".formattedPrice")
  priceElements.forEach((element) => formatPriceInToman(element));
});