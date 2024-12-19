Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a **maximum score of 800 points**. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.

Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend. 

You have been provided with a dataset called `schools.csv`.

You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.

<p>Which NYC schools have the best math results?  </p>

<ul><li>The best math results are at least 80% of the <strong>*maximum possible score of 800</strong>* for math.</li><li>Save your results in a pandas DataFrame called <code>best_math_schools</code>, including <code>"school_name"</code> and <code>"average_math"</code> columns, sorted by <code>"average_math"</code> in descending order.</li></ul>

<p>What are the top 10 performing schools based on the combined SAT scores? </p>

<ul><li>Save your results as a pandas DataFrame called <code>top_10_schools</code> containing the <code>"school_name"</code> and a new column named <code>"total_SAT"</code>, with results ordered by <code>"total_SAT"</code> in descending order (<code>"total_SAT"</code> being the sum of math, reading, and writing scores).</li></ul>

<p>Which single borough has the largest standard deviation in the combined SAT score?</p>

<ul><li>Save your results as a pandas DataFrame called <code>largest_std_dev</code>.</li><li>The DataFrame should contain one row, with:<ul><li><code>"borough"</code> - the name of the NYC borough with the largest standard deviation of <code>"total_SAT"</code>.</li><li><code>"num_schools"</code> - the number of schools in the borough.</li><li><code>"average_SAT"</code> - the mean of <code>"total_SAT"</code>.</li><li><code>"std_SAT"</code> - the standard deviation of <code>"total_SAT"</code>.</li></ul></li><li>Round all numeric values to two decimal places.</li></ul></div>