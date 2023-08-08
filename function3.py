{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cef06612",
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_data(df):\n",
    "    \n",
    "    df = df[['BP','Age','Height','Weight','foot','Growth','Value','Attacking','Skill','Movement','Power','Mentality','Defending',\n",
    "              'Goalkeeping','Total Stats','Base Stats', 'W/F', 'SM', 'A/W','D/W', 'IR', 'PAC', 'SHO', 'PAS', 'DRI', 'DEF',\n",
    "              'PHY','OVA']]\n",
    "    def feet_to_cm(height_str):\n",
    "        feet, inches = map(int, height_str.replace('\"', '').split(\"'\"))\n",
    "        total_inches = (feet * 12) + inches\n",
    "        cm = total_inches * 2.54\n",
    "        return cm\n",
    "    df['Height'] = df['Height'].apply(feet_to_cm)\n",
    "    \n",
    "    df['Weight']=df['Weight'].str.replace(\"lbs\",\"\")\n",
    "    df['Weight']=pd.to_numeric(df['Weight'], errors='coerce')\n",
    "    \n",
    "    def value_calc(value_str):\n",
    "        value = value_str.replace(\"€\",\"\")\n",
    "        if 'M' in value:\n",
    "            value = value.replace(\"M\",\"\")\n",
    "            value = pd.to_numeric(value, errors='coerce')\n",
    "            value = value * 1000000\n",
    "        elif 'K' in value:\n",
    "            value = value.replace(\"K\",\"\")\n",
    "            value = pd.to_numeric(value, errors='coerce')        \n",
    "            value = value * 1000\n",
    "        else:\n",
    "            value = pd.to_numeric(value, errors='coerce')        \n",
    "        return value\n",
    "    df['Value'] = df['Value'].apply(value_calc)\n",
    "    \n",
    "    df['W/F'] = df['W/F'].str.replace(\" ★\",\"\")\n",
    "    df['W/F']=pd.to_numeric(df['W/F'], errors='coerce')\n",
    "    df['SM'] = df['SM'].str.replace(\"★\",\"\")\n",
    "    df['SM']=pd.to_numeric(df['SM'], errors='coerce')\n",
    "    df['IR'] = df['IR'].str.replace(\" ★\",\"\")\n",
    "    df['IR']=pd.to_numeric(df['IR'], errors='coerce')\n",
    "    \n",
    "    df['A/W'] = df['A/W'].fillna('Medium')\n",
    "    df['D/W'] = df['D/W'].fillna('Medium')\n",
    "        \n",
    "    return df"
   ]
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
