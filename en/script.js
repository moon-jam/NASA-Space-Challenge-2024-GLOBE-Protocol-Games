document.addEventListener('DOMContentLoaded', function () {
    const taskCard = document.body.getAttribute('data-task');
    const startButton = document.getElementById('start-button');
    const startContainer = document.getElementById('start-container');
    const questionContainer = document.getElementById('question-container');
    const questionElement = document.getElementById('question');
    const feedbackElement = document.getElementById('feedback');
    const timerElement = document.getElementById('timer');
    const alertSound = new Audio('../alert.wav'); // Audio file path
    let remainingTime = 20;
    let timer;

    startButton.addEventListener('click', function () {
      // Show question container and hide start container
      startContainer.style.display = 'none';
      questionContainer.style.display = 'block';

      // Load questions and start timer
      fetch('../QA.json')
        .then(response => response.json())
        .then(data => {
          const questions = data[taskCard];
          const randomQuestion = questions[Math.floor(Math.random() * questions.length)];
          questionElement.textContent = randomQuestion.question;
          document.getElementById('reveal').addEventListener('click', function () {
            clearInterval(timer);
            feedbackElement.textContent = `Answer: ${randomQuestion.answer}`;
          });
          startTimer();
        });
    });
  
    // Countdown timer
    function startTimer() {
      timer = setInterval(() => {
        remainingTime--;
        timerElement.textContent = remainingTime;
        if (remainingTime <= 0) {
          clearInterval(timer);
          feedbackElement.textContent = "Time's up!";
          alertSound.play(); // Play sound effect
        }
      }, 1000);
    }
});