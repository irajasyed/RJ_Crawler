import os
os.system("""
cd ~/AnnaUniversity
git pull
cp ~/PycharmProjects/URL_Test/log_rj.txt log_rj.txt &&

git add . &&
git commit . -m "log_test" &&
git push --repo https://rajasyed:'payoda8080'@github.com/rajasyed/AnnaUniversity.git""")
