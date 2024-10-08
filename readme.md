-- To check the files in a directory we used linux called ls -a
-- git status is to check whether or not we have added all the files to the staging area
-- git log is to check the commits we performed till now.
-- git branch to check the branch you are working in
-- git branch branch_name - you will create a new branch
-- git checkout branch_name- to move to a different branch
-- git merge branchname -- to merge the branches
python -m venv myenv - to create a virtual environment
myenv\Scripts\activate - fpor windows
source myenv/bin/activate
echo. > eda.ipynb -- to creata a new file
git push -u origin main - push the code to the central repository
 git clone https://github.com/mujeebr/linear_regression.git - to cpy the code
st.selectbox("Education",("Graduate","Not Graduate"))
st.selectbox("Self Employed",("Yes","No"))
fig = px.scatter_3d(df, x='feature1', y='feature2', z='target')
fig.add_trace(go.Surface(x = x, y = y, z =z ))
fig.show()
plt.scatter(df['cgpa'],df['package'])
plt.plot(X_train,lr.predict(X_train),color='red')
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')
pip install "numpy<2" pyarrow
pip uninstall numpy pyarrow
pip install numpy<2 pyarrow

docker run -d -P --name catgif manifoldailearning/catgif
docker ps
docker port catgif
docker stop catgif
docker run -p 8888:5000 manifoldailearning/catgif
docker build -t catgifv2 .
docker run -p 8888:5000 catgifv2
docker login
docker build -t manifoldailearning/catgif-devops .
docker push manifoldailearning/catgif-devops
