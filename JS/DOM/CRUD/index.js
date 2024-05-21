const doc = document;
const type = doc.querySelector("form input[id='type']");
const title = doc.querySelector("form input[id='title']");
const imageLink = doc.querySelector("form input[id='imageLink']");
const description = doc.querySelector("form textarea[id='description']");
const avatarLink = doc.querySelector("form input[id='avatarLink']");
const avatarName = doc.querySelector("form input[id='avatarName']");
const createdAt = doc.querySelector("form input[id='createdAt']");
const submitBtn = doc.querySelector(".submit-btn");
const closeBtn = doc.querySelector(".close-btn");
const foodCardLists = doc.querySelector(".food-recipe");
const recipes = [];

function CardItem(data) {
  const { title, type, description, author, avatar, image, createdAt } = data;
  return `<section class="card-item">
            <img class="image" src="${image}" width="100%" alt="img">
            <article class="content">
                <p class="title">${type}</p>
                <p>${title}</p>
                <p class="description">${description}</p>
                <article class="profile">
                    <img src="${avatar}"
                        alt="img" width="100%" class="avatar">
                    <div class="details">
                        <p class="title">${author}</p>
                        <p class="subtitle">${createdAt}</p>
                    </div>
                </article>
            </article>
        </section>`;
}

submitBtn.addEventListener("click", function () {
  const data = {
    type: type.value,
    title: title.value,
    description: description.value,
    author: avatarName.value,
    avatar: avatarLink.value,
    image: imageLink.value,
    createdAt: createdAt.value,
  };

  //   localStorage.setItem(
  //     "array",
  //     JSON.stringify([...localStorage.getItem("array"), data])
  //   );

  //   foodCardLists.innerHTML = JSON.parse(localStorage.getItem("array"))
  //     .map(CardItem)
  //     .join("");

  recipes.push(data);

  foodCardLists.innerHTML = recipes.map(CardItem).join("");
});

// foodCardLists.innerHTML = JSON.parse(localStorage.getItem("array"))
//   .map(CardItem)
//   .join("");
