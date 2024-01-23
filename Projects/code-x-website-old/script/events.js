document.addEventListener("DOMContentLoaded", function () {
    const eventList = document.getElementById("event-list");

    const events = [
        {
            title: "Summer Car Show",
            date: "September 16, 2023",
            description: "Join us for a car show featuring the latest car models and special discounts."
        },
        {
            title: "Off-Roading Adventure",
            date: "September 24, 2023",
            description: "Experience an exciting off-roading adventure with our rental SUVs."
        },
        {
            title: "Spring Road Trip Special",
            date: "October 20, 2023",
            description: "Plan your spring road trip with our special rental rates and packages."
        },
        {
            title: "Rock Paper Scissors Event",
            date: "October 20, 2023",
            description: "Plan your spring road trip with our special rental rates and packages."
        }
    ];

    events.forEach(event => {
        const eventCard = document.createElement("div");
        eventCard.classList.add("event");

        const title = document.createElement("h2");
        title.textContent = event.title;

        const date = document.createElement("p");
        date.textContent = "Date: " + event.date;

        const description = document.createElement("p");
        description.textContent = event.description;

        const subscribeButton = document.createElement("button");
        subscribeButton.textContent = "Join";
        subscribeButton.addEventListener("click", () => {
            alert("You have joined the event: " + event.title);
        });

        if (event.title === "Rock Paper Scissors Event") {
            subscribeButton.textContent = "Play Now";
            subscribeButton.addEventListener("click", () => {
                window.location.href = "game.html"; // Redirect to the new page
            });
        }


        eventCard.appendChild(title);
        eventCard.appendChild(date);
        eventCard.appendChild(description);
        eventCard.appendChild(subscribeButton);
        
        eventList.appendChild(eventCard);
    });
});

