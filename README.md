<h1>Franchise500 Spider</h1>

<p>This repository contains a web scraping spider built using Scrapy, a Python framework for extracting data from websites. The spider is designed to crawl and scrape data from the <a href="https://www.entrepreneur.com/franchise500">Entrepreneur Franchise 500</a> webpage.</p>

<h2>Requirements</h2>

<p>To run this project, you need to have the following dependencies installed:</p>

<ul>
  <li>Python 3.x</li>
  <li>Scrapy</li>
</ul>

<h2>Project Structure</h2>

<p>The repository has the following structure:</p>

<ul>
  <li><code>franchise.py</code>: Scrapy spider that defines the crawling behavior and data extraction logic.</li>
  <li><code>items.py</code>: Item class that represents the structure of the scraped data.</li>
  <li><code>settings.py</code>: A configuration file for the Scrapy project, allowing to customize the behavior of the project by modifying various settings.</li>
</ul>

<p>To run the spider, navigate to the project directory in the terminal and execute the following command:</p>

<pre>
<code>scrapy crawl franchise -O franchises.csv</code>
</pre>

<p>The spider will start scraping franchise data from Entreprenuer.com and save it as a csv file.</p>

<h2>Scraped Data</h2>

<p>The scraped data is available in the <a href="https://github.com/serkansalcan/franchise500-scraper/blob/main/franchises.csv">franchises.csv</a> file in this repository. You can download and explore the extracted information.</p>

