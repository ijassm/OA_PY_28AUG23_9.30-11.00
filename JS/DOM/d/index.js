import data from "./data.js";

const doc = document;

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

const cardList = doc.querySelectorAll(".card-wrapper")[0];
const cardList2 = doc.querySelectorAll(".card-wrapper")[1];

cardList.innerHTML = data.map(CardItem).join("");
cardList2.innerHTML = data.map(CardItem).join("");

// data.map(function (data, index, arr) {
//   console.log("data : ", data);
//   console.log("index : ", index);
//   console.log("arr : ", arr);
//   console.log("\n");
// });
