# steps

1) clone this repo

`git clone https://github.com/c4software/python-sitemap.git`

2) enter repo directory
`cd  python-sitemap`

3) run main.py specifying a website and output file of your choice. example:

`python3 main.py --domain https://www.epa.gov --output www.epa.gov.xml`

4) the above output has been saved here for your convenience:

[link to raw view of xml](https://raw.githubusercontent.com/openciti/epa/master/www.epa.gov.xml)

4) convert to csv:

`python3 tocsv.py`

5) the above output has been saved here for your convenience:

[link to raw view of csv](https://raw.githubusercontent.com/openciti/epa/master/www.epa.gov.csv)

6) optional. strip out links to files

`./nofiles.sh`

7) the above output has been save here for your convenience:

[link to raw txt](https://raw.githubusercontent.com/openciti/epa/master/cleaned_nofiles.txt)

8) TODO: the above script is runing on an aws server check its public web site for some UI (coming soon)


here: http://52.60.90.44/~ubuntu/

or

here: http://52.60.90.44
