document.addEventListener('DOMContentLoaded', function () {
    const taskCard = document.body.getAttribute('data-task');
    const startButton = document.getElementById('start-button');
    const startContainer = document.getElementById('start-container');
    const questionContainer = document.getElementById('question-container');
    const questionElement = document.getElementById('question');
    const feedbackElement = document.getElementById('feedback');
    const timerElement = document.getElementById('timer');
    const alertSound = new Audio('../alert.wav');  // 音效檔案路徑
    let remainingTime = 20;
    let timer;

    startButton.addEventListener('click', function () {
        // 顯示問題容器並隱藏開始容器
        startContainer.style.display = 'none';
        questionContainer.style.display = 'block';
        
        // 載入問題並啟動計時器
        fetch('../QA.json')
            .then(response => response.json())
            .then(data => {
                const questions = data[taskCard];
                const randomQuestion = questions[Math.floor(Math.random() * questions.length)];
                questionElement.textContent = randomQuestion.question;
                document.getElementById('reveal').addEventListener('click', function () {
                    clearInterval(timer);
                    feedbackElement.textContent = `答案：${randomQuestion.answer}，分數：${randomQuestion.score} 分`;
                });
                startTimer();
            });
    });

    // 倒數計時器
    function startTimer() {
        timer = setInterval(() => {
            remainingTime--;
            timerElement.textContent = remainingTime;
            if (remainingTime <= 0) {
                clearInterval(timer);
                feedbackElement.textContent = "時間到！";
                alertSound.play();  // 播放音效
            }
        }, 1000);
    }
});
