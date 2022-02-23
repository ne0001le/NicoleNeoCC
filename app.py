{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f1d392e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "cd4e0ec4",
   "metadata": {},
   "outputs": [],
   "source": [
    "app=Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c662da3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request,render_template\n",
    "import joblib\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method==\"POST\":\n",
    "        Income = request.form.get(\"Income\")\n",
    "        Age = request.form.get(\"Age\")\n",
    "        Loan = request.form.get(\"Loan\")\n",
    "        print(Income,Age,Loan) \n",
    "        model=joblib.load(\"Creditcard\")\n",
    "        pred=model.predict([[float(Income),float(Age),float(Loan)]])\n",
    "        print(pred)\n",
    "        s=\"The predicted default score is:\"+str(pred)\n",
    "        return(render_template(\"index.html\",result=s))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result=\"2\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed856730",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__==\"__main__\":\n",
    "    app.run()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08038493",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23ab8711",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
