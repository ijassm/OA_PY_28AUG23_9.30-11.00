import recipes from "./mockData/recipes.js";
import blogs from "./mockData/blogs.js";

const doc = document;
// const section = doc.createElement("section");
// const img = doc.createElement("img");
// img.src = "";
// img.className = "";
// img.alt = "";

// section.append(img, );

function CardItem(data) {
  const { title, description, author, avatar, image } = data;
  return `<section class="card-item">
            <img class="image" src="${image}" width="100%" alt="img">
            <article class="content">
                <p class="title">Cooking, Recipe</p>
                <p>${title}</p>
                <p class="description">${description}</p>
                <article class="profile">
                    <img src="${avatar}"
                        alt="img" width="100%" class="avatar">
                    <div class="details">
                        <p class="title">${author}</p>
                        <p class="subtitle">Aug 18</p>
                    </div>
                </article>
            </article>
        </section>`;
}

const foodCardLists = doc.querySelector(".food-recipe");
const blogLists = doc.querySelector(".blog");

foodCardLists.innerHTML = recipes.map(CardItem).join("");
blogLists.innerHTML = blogs.map(CardItem).join("");

// data.map(function (data, index, arr) {
//   console.log("data : ", data);
//   console.log("index : ", index);
//   console.log("arr : ", arr);
//   console.log("\n");
// });
