console.log("Hello World!!")

function searchProducts(e) {
    let input = document.getElementById("navbar-search")
    let filter = input.value.toLowerCase()
    let products = document.querySelectorAll(".product-small")
    products.forEach(product => {
        let productName = product.querySelector(".card-title").textContent.toLowerCase();
        let productDesc = product.querySelector(".card-text").textContent.toLowerCase();
        if (productName.indexOf(filter) > -1 || productDesc.indexOf(filter) > -1) {
            product.style.display = "block"
        } else {
            product.style.display = "none"

        }
    });
}

function filterLTH() {
    // Get all the products and then sort it in the price ascending order. then replace it
    let productsList = document.querySelector("")
}