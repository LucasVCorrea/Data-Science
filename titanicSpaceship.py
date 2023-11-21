{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LucasVCorrea/Data-Science/blob/main/titanicSpaceship.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rD73ygNKF03V"
      },
      "source": [
        "# Carga de datos"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 631,
      "metadata": {
        "id": "rBdyAnuKWtzO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5fa3f49c-7080-4b2d-e20d-a23c9a1c05a3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount(\"/content/drive\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 632,
      "metadata": {
        "id": "RGev_zr8XGXi"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "train_csv = pd.read_csv('/content/drive/MyDrive/Organizacion De Datos/SpaceshipTitanic/train.csv')\n",
        "test_csv = pd.read_csv('/content/drive/MyDrive/Organizacion De Datos/test.csv')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 633,
      "metadata": {
        "id": "Su70WQ1AIc64"
      },
      "outputs": [],
      "source": [
        "my_train = train_csv\n",
        "my_test = test_csv"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 634,
      "metadata": {
        "id": "QktG2aBwFkXU",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "outputId": "aa6ee850-c8a6-45fb-f58d-9c8d0f3b86c8"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  PassengerId HomePlanet CryoSleep  Cabin  Destination   Age    VIP  \\\n",
              "0     0001_01     Europa     False  B/0/P  TRAPPIST-1e  39.0  False   \n",
              "1     0002_01      Earth     False  F/0/S  TRAPPIST-1e  24.0  False   \n",
              "2     0003_01     Europa     False  A/0/S  TRAPPIST-1e  58.0   True   \n",
              "3     0003_02     Europa     False  A/0/S  TRAPPIST-1e  33.0  False   \n",
              "4     0004_01      Earth     False  F/1/S  TRAPPIST-1e  16.0  False   \n",
              "\n",
              "   RoomService  FoodCourt  ShoppingMall     Spa  VRDeck               Name  \\\n",
              "0          0.0        0.0           0.0     0.0     0.0    Maham Ofracculy   \n",
              "1        109.0        9.0          25.0   549.0    44.0       Juanna Vines   \n",
              "2         43.0     3576.0           0.0  6715.0    49.0      Altark Susent   \n",
              "3          0.0     1283.0         371.0  3329.0   193.0       Solam Susent   \n",
              "4        303.0       70.0         151.0   565.0     2.0  Willy Santantines   \n",
              "\n",
              "   Transported  \n",
              "0        False  \n",
              "1         True  \n",
              "2        False  \n",
              "3        False  \n",
              "4         True  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-158a320b-1590-4037-865d-ca37c285d0d7\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>HomePlanet</th>\n",
              "      <th>CryoSleep</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Destination</th>\n",
              "      <th>Age</th>\n",
              "      <th>VIP</th>\n",
              "      <th>RoomService</th>\n",
              "      <th>FoodCourt</th>\n",
              "      <th>ShoppingMall</th>\n",
              "      <th>Spa</th>\n",
              "      <th>VRDeck</th>\n",
              "      <th>Name</th>\n",
              "      <th>Transported</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0001_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>B/0/P</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>39.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Maham Ofracculy</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0002_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>F/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>24.0</td>\n",
              "      <td>False</td>\n",
              "      <td>109.0</td>\n",
              "      <td>9.0</td>\n",
              "      <td>25.0</td>\n",
              "      <td>549.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>Juanna Vines</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0003_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>58.0</td>\n",
              "      <td>True</td>\n",
              "      <td>43.0</td>\n",
              "      <td>3576.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>6715.0</td>\n",
              "      <td>49.0</td>\n",
              "      <td>Altark Susent</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0003_02</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>33.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1283.0</td>\n",
              "      <td>371.0</td>\n",
              "      <td>3329.0</td>\n",
              "      <td>193.0</td>\n",
              "      <td>Solam Susent</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0004_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>F/1/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>16.0</td>\n",
              "      <td>False</td>\n",
              "      <td>303.0</td>\n",
              "      <td>70.0</td>\n",
              "      <td>151.0</td>\n",
              "      <td>565.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>Willy Santantines</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-158a320b-1590-4037-865d-ca37c285d0d7')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-158a320b-1590-4037-865d-ca37c285d0d7 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-158a320b-1590-4037-865d-ca37c285d0d7');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-a84b82a5-4467-4b24-865b-15c6c74726fc\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-a84b82a5-4467-4b24-865b-15c6c74726fc')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-a84b82a5-4467-4b24-865b-15c6c74726fc button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 634
        }
      ],
      "source": [
        "my_train.head(5)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ckYSuCWlFt-a"
      },
      "source": [
        "## Expo analisis"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 635,
      "metadata": {
        "id": "lh39uanWFrzM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "37617833-dddb-434d-bde2-f1ae18e6aa17"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 635
        }
      ],
      "source": [
        "my_train.HomePlanet.nunique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 636,
      "metadata": {
        "id": "FngdbDmFF_1L",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d073eda6-f19b-4948-d429-d320aa8492a4"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Europa', 'Earth', 'Mars', nan], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 636
        }
      ],
      "source": [
        "my_train.HomePlanet.unique()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1OsgHOPmHjS_"
      },
      "source": [
        "Pasajeros por planeta"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 637,
      "metadata": {
        "id": "l7mVY6uPO653"
      },
      "outputs": [],
      "source": [
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 638,
      "metadata": {
        "id": "ts-agR9KGMHJ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 489
        },
        "outputId": "07f6988b-ea6f-404f-f17f-c3f44d20d967"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[Text(0.5, 1.0, 'Distribucion de homePlanet')]"
            ]
          },
          "metadata": {},
          "execution_count": 638
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkQAAAHHCAYAAABeLEexAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA6/klEQVR4nO3deXxNdx7/8ffNvrkJQSIEqTWxVrpIS20hNDo65We0lljbalC0tIai2hmt1tai2jEVM2WobrTUvtVS1ZApiqqhUSSxx5qQnN8f/eX8XIklkeSG83o+HvfxyP2ez/2ez7n3NH0795wTm2EYhgAAACzMxdkNAAAAOBuBCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCChmY8eOlc1mK5Z1NW/eXM2bNzefr1u3TjabTZ999lmxrP9aNptNY8eOLfb13kjPnj1VtWrVQp3Pz8+v0OYriXL2n3Xr1jm7FaDQEYiAO5CQkCCbzWY+vLy8FBISopiYGL333ns6d+5coazn6NGjGjt2rJKSkgplPuBaee3HNWvW1IABA5Samurs9m5oxowZSkhIcHYbuEe4ObsB4F4wbtw4hYWF6cqVK0pJSdG6des0ePBgTZo0SYsXL1b9+vXN2lGjRunVV1/N1/xHjx7V66+/rqpVq6phw4a3/boVK1bkaz1F6dKlS3Jz41dOSZazH1++fFkbN27UBx98oKVLl2rXrl3y8fFxdnu5zJgxQ2XLllXPnj2d3QruAfx2AgpBu3bt9MADD5jPR4wYoTVr1qh9+/b605/+pD179sjb21uS5ObmVuTB4OLFi/Lx8ZGHh0eRric/vLy8nN0CbuHa/bhv374KDAzUpEmTtGjRIj399NNO7g4oWnxlBhSRli1b6rXXXtNvv/2mTz75xBzP6xyilStXqkmTJgoICJCfn59q1aqlv/71r5L+OG/jwQcflCT16tXL/Foj56uC5s2bq27dukpMTNRjjz0mHx8f87XXn0OUIysrS3/9618VHBwsX19f/elPf9Lhw4cdaqpWrZrnv7zzmvPy5csaO3asatasKS8vL1WoUEFPPfWUDhw4YNbkdQ7Rjh071K5dO9ntdvn5+alVq1b6/vvvHWpyvs7ZtGmThg4dqnLlysnX11d//vOfdfz48Vz95eWrr75S3bp15eXlpbp16+rLL7/Msy47O1tTpkxRnTp15OXlpaCgID333HM6ffr0ba1Hko4cOaInn3xSfn5+KleunF5++WVlZWU51Fy4cEEvvfSSQkND5enpqVq1aundd9+VYRgOdTabTQMGDNDChQsVEREhb29vRUVFaefOnZKkDz/8UNWrV5eXl5eaN2+uQ4cO5epn69atatu2rfz9/eXj46NmzZpp06ZNt7UtLVu2lCQdPHjwhjXfffed/s//+T+qXLmyPD09FRoaqiFDhujSpUsOdTnnWN3O+3M7n0PVqlW1e/durV+/3vxvIq99HbhdHCECilD37t3117/+VStWrFC/fv3yrNm9e7fat2+v+vXra9y4cfL09NSvv/5q/k8rPDxc48aN0+jRo/Xss8+qadOmkqRHHnnEnOPkyZNq166dunTpom7duikoKOimff3tb3+TzWbTK6+8orS0NE2ZMkXR0dFKSkoyj2TdrqysLLVv316rV69Wly5d9OKLL+rcuXNauXKldu3apWrVqt1wu5s2bSq73a7hw4fL3d1dH374oZo3b67169fr4YcfdqgfOHCgSpcurTFjxujQoUOaMmWKBgwYoAULFty0vxUrVqhjx46KiIjQ+PHjdfLkSfXq1UuVKlXKVfvcc88pISFBvXr10qBBg3Tw4EFNmzZNO3bs0KZNm+Tu7n7L9yImJkYPP/yw3n33Xa1atUoTJ05UtWrV1L9/f0mSYRj605/+pLVr16pPnz5q2LChli9frmHDhunIkSOaPHmyw5zfffedFi9erPj4eEnS+PHj1b59ew0fPlwzZszQCy+8oNOnT2vChAnq3bu31qxZY752zZo1ateunSIjIzVmzBi5uLho9uzZatmypb777js99NBDN92enEAbGBh4w5qFCxfq4sWL6t+/vwIDA/XDDz/o/fff1++//66FCxfm+/253c9hypQpGjhwoPz8/DRy5EhJuuV+D9yUAaDAZs+ebUgytm3bdsMaf39/4/777zefjxkzxrj2P73Jkycbkozjx4/fcI5t27YZkozZs2fnWtasWTNDkjFz5sw8lzVr1sx8vnbtWkOSUbFiRSM9Pd0c//TTTw1JxtSpU82xKlWqGHFxcbec8+OPPzYkGZMmTcpVm52dbf4syRgzZoz5/MknnzQ8PDyMAwcOmGNHjx41SpUqZTz22GPmWM57HB0d7TDfkCFD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kZFyd3fX6tWrzbF9+/YpOTlZUVFRkqSoqCjt3LlTaWlpZs3KlStlt9sVERFh1lw7R05NzhzX8/T0lN1ud3gAAIB7l1PPIYqPj9e8efO0aNEilSpVyjznx9/fX97e3vL391efPn00dOhQlSlTRna7XQMHDlRUVJQaN24sSWrTpo0iIiLUvXt3TZgwQSkpKRo1apTi4+Pl6ekpSXr++ec1bdo0DR8+XL1799aaNWv06aefasmSJU7bdgAAUHI49QjRBx98oLNnz6p58+aqUKGC+ViwYIFZM3nyZLVv314dO3bUY489puDgYH3xxRfmcldXV33zzTdydXVVVFSUunXrph49emjcuHFmTVhYmJYsWaKVK1eqQYMGmjhxombNmsUl9wAAQJKTjxAZhnHLGi8vL02fPl3Tp0+/YU2VKlW0dOnSm87TvHlz7dixI989AgCAe1+JOKkaAADAmQhEAADA8ghEAADA8ghEAADA8ghEAADA8ghEAADA8ghEAADA8ghEAADA8ghEAADA8ghEAADA8ghEAADA8pz6t8wAAHenPXv2OLsF3GPKli2rypUrO239BCIAwG07diFTLpK6devm7FZwj/Hx9tKevfucFooIRACA23bm8lVlS/pHy6pqVDHQ2e3gHrHn5EV1W7pHJ06cIBABAO4etQK81SiolLPbAAoNJ1UDAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLc2og2rBhg5544gmFhITIZrPpq6++clhuGIZGjx6tChUqyNvbW9HR0dq/f79DzalTp9S1a1fZ7XYFBASoT58+On/+vEPNTz/9pKZNm8rLy0uhoaGaMGFCUW8aAAC4izg1EF24cEENGjTQ9OnT81w+YcIEvffee5o5c6a2bt0qX19fxcTE6PLly2ZN165dtXv3bq1cuVLffPONNmzYoGeffdZcnp6erjZt2qhKlSpKTEzUO++8o7Fjx+qjjz4q8u0DAAB3Bzdnrrxdu3Zq165dnssMw9CUKVM0atQodejQQZL0r3/9S0FBQfrqq6/UpUsX7dmzR8uWLdO2bdv0wAMPSJLef/99Pf7443r33XcVEhKiuXPnKjMzUx9//LE8PDxUp04dJSUladKkSQ7BCQAAWFeJPYfo4MGDSklJUXR0tDnm7++vhx9+WFu2bJEkbdmyRQEBAWYYkqTo6Gi5uLho69atZs1jjz0mDw8PsyYmJkb79u3T6dOn81x3RkaG0tPTHR4AAODeVWIDUUpKiiQpKCjIYTwoKMhclpKSovLlyzssd3NzU5kyZRxq8prj2nVcb/z48fL39zcfoaGhd75BAACgxCqxgciZRowYobNnz5qPw4cPO7slAABQhEpsIAoODpYkpaamOoynpqaay4KDg5WWluaw/OrVqzp16pRDTV5zXLuO63l6esputzs8AADAvavEBqKwsDAFBwdr9erV5lh6erq2bt2qqKgoSVJUVJTOnDmjxMREs2bNmjXKzs7Www8/bNZs2LBBV65cMWtWrlypWrVqqXTp0sW0NQAAoCRzaiA6f/68kpKSlJSUJOmPE6mTkpKUnJwsm82mwYMH680339TixYu1c+dO9ejRQyEhIXryySclSeHh4Wrbtq369eunH374QZs2bdKAAQPUpUsXhYSESJKeeeYZeXh4qE+fPtq9e7cWLFigqVOnaujQoU7aagAAUNI49bL7H3/8US1atDCf54SUuLg4JSQkaPjw4bpw4YKeffZZnTlzRk2aNNGyZcvk5eVlvmbu3LkaMGCAWrVqJRcXF3Xs2FHvvfeeudzf318rVqxQfHy8IiMjVbZsWY0ePZpL7gEAgMmpgah58+YyDOOGy202m8aNG6dx48bdsKZMmTKaN2/eTddTv359fffddwXuEwAA3NtK7DlEAAAAxYVABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAA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/LjRoUMHIy4uLs/XHj9+3JBk7Ny50zCM/7//TJkyxaGuXr16xtixY4t6U3ALnJSBItGiRQt98MEHDmNlypRRenr6bc/xwAMPmD8fOHBAV65c0aOPPmqOubu766GHHtKePXscXhcVFeWwzlq1apk1WVlZ+vvf/65PP/1UR44cUWZmpjIyMuTj45Ov7UPJcqP9TZJWrVql8ePHa+/evUpPT9fVq1d1+fJlXbx40fzcPTw8VL9+/dte37W1FSpUkCSlpaWpdu3ad7opKKHKlSun2NhYJSQkyDAMxcbGqmzZsg41+/fv1+jRo7V161adOHHCPDKUnJysunXrmnXX/m6TpEGDBql///5asWKFoqOj1bFjx3ztjygcBCIUCV9fX1WvXj3XeM65G8Y1fzEm5+usvOYobO+8846mTp2qKVOmmOeVDB48WJmZmYW+LhSfG+1vhw4dUvv27dW/f3/97W9/U5kyZbRx40b16dNHmZmZZiDy9vbO14nU154Em/O6678Wwb2nd+/e5t/DnD59eq7lTzzxhKpUqaJ//OMfCgkJUXZ2turWrZvr98v1v9v69u2rmJgYLVmyRCtWrND48eM1ceJEDRw4sOg2BrlwDhGKVbly5SRJx44dM8du554u1apVk4eHhzZt2mSOXblyRdu2bVNERIRD7ffff2/+fPr0af3yyy8KDw+XJG3atEkdOnRQt27d1KBBA91333365Zdf7mSTUIIlJiYqOztbEydOVOPGjVWzZk0dPXr0tl7r4eGhrKysIu4Qd5O2bdsqMzNTV65cUUxMjMOykydPat++fRo1apRatWql8PBwnT59+rbnDg0N1fPPP68vvvhCL730kv7xj38Udvu4BY4QoUhkZGQoJSXFYczNzU1ly5ZV48aN9dZbbyksLExpaWkaNWrULefz9fVV//79NWzYMJUpU0aVK1fWhAkTdPHiRfXp08ehdty4cQoMDFRQUJBGjhypsmXLmveTqVGjhj777DNt3rxZpUuX1qRJk5SamporVOHucqP9rXr16rpy5Yref/99PfHEE9q0aZNmzpx5W3NWrVpVy5cv1759+xQYGCh/f/+iaB13EVdXV/Prd1dXV4dlpUuXVmBgoD766CNVqFBBycnJevXVV29r3sGDB6tdu3aqWbOmTp8+rbVr15r/iEPx4QgRisSyZctUoUIFh0eTJk0k/XF1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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.histplot(data = my_train, x = 'HomePlanet', color = 'OrangeRed').set(title = 'Distribucion de homePlanet')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2gWs3VH-K_jy"
      },
      "source": [
        "Pasajeros salvados y no salvados por planeta"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 639,
      "metadata": {
        "id": "Uz2xDfaZIyug"
      },
      "outputs": [],
      "source": [
        "transportados_por_planeta = my_train.groupby(['HomePlanet', 'Transported']).agg({'PassengerId':['count']})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 640,
      "metadata": {
        "id": "cQcwkp0gJc5n"
      },
      "outputs": [],
      "source": [
        "transportados_por_planeta = transportados_por_planeta.reset_index()\n",
        "transportados_por_planeta.columns = ['planeta_home', 'transportado', 'cantidad']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 641,
      "metadata": {
        "id": "0NjUTpCbJnyI",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 489
        },
        "outputId": "e5726665-b007-4486-a01e-caa253210c27"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[Text(0.5, 1.0, 'Resultados por planeta')]"
            ]
          },
          "metadata": {},
          "execution_count": 641
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkQAAAHHCAYAAABeLEexAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABL80lEQVR4nO3deVhVVf/+8fuAMgsIMjiQ4oyKlphKmkOaOKalNpnz8OSYmuPzOJuRlnOWlaVWVmqjqTlPaU5pmBqaA6aV4AyiKQj794df9q8TaojIQff7dV3nuthrr7P2Zx12crenYzMMwxAAAICFOTm6AAAAAEcjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAG4LTabTWPGjMmVbZUoUUKdOnXKlW3di/h8gJxDIALykHnz5slms5mvfPnyqWjRourUqZP++OMPR5d3Qz/88IPGjBmjCxcuOLoUOBD7Ae51BCIgDxo3bpw++ugjzZ49W02aNNHHH3+sunXr6sqVK44uLZMffvhBY8eO5Q+hxbEf4F6Xz9EFAMisSZMmqlatmiSpW7duKlSokCZOnKglS5bo6aefdnB1uFOXLl2Sp6eno8sA8DccIQLuAY8++qgk6ciRI3btBw4cUJs2beTn5yc3NzdVq1ZNS5YsseuTmpqqsWPHqkyZMnJzc5O/v79q166t1atXm33q1aunevXqZdpup06dVKJEiZvWNWbMGA0ePFiSFBoaap7qO3bsmCRp7ty5euyxxxQYGChXV1dVqFBBb7/9dqZxDMPQK6+8omLFisnDw0P169fX/v37b7jNo0ePqm3btvLz85OHh4dq1qypZcuWZeo3c+ZMVaxYUR4eHipYsKCqVaumTz755KZzkaQNGzbIZrNp4cKF+u9//6vg4GB5enrqiSee0IkTJzL1X7x4sSIiIuTu7q5ChQrphRdeyHRqs1OnTvLy8tKRI0fUtGlTFShQQO3atbtpDWPGjJHNZtOBAwf09NNPy9vbW/7+/nrppZf+9QjhuXPnNGjQIIWHh8vLy0ve3t5q0qSJ9uzZc8N5Llq0SBMmTFCxYsXk5uamBg0a6PDhw5nG3b59uxo3biwfHx95eHiobt262rJli13NObEfAI7EESLgHpDxh6VgwYJm2/79+1WrVi0VLVpUw4YNk6enpxYtWqRWrVrpiy++0JNPPinp+h+r6OhodevWTdWrV1dSUpJ+/PFH7d69W48//vgd1fXUU0/p119/1aeffqqpU6eqUKFCkqSAgABJ0ttvv62KFSvqiSeeUL58+fTtt9+qV69eSk9PV+/evc1xRo0apVdeeUVNmzZV06ZNtXv3bjVq1EgpKSl220tISNAjjzyiy5cvq1+/fvL399f8+fP1xBNP6PPPPzfn/N5776lfv35q06aNGSR+/vlnbd++Xc8///y/zmvChAmy2WwaOnSoTp06pWnTpqlhw4aKiYmRu7u7pOvXe3Xu3FkPP/ywoqOjlZCQoOnTp2vLli366aef5Ovra4537do1RUVFqXbt2nrjjTfk4eHxrzU8/fTTKlGihKKjo7Vt2zbNmDFD58+f14cffnjT9xw9elRff/212rZtq9DQUCUkJOidd95R3bp19csvv6hIkSJ2/V977TU5OTlp0KBBSkxM1KRJk9SuXTtt377d7LNu3To1adJEERERGj16tJycnMyA8/3336t69eo5th8ADmUAyDPmzp1rSDLWrFljnD592jhx4oTx+eefGwEBAYarq6tx4sQJs2+DBg2M8PBw48qVK2Zbenq68cgjjxhlypQx26pUqWI0a9bsltutW7euUbdu3UztHTt2NIoXL27XJskYPXq0ufz6668bkoy4uLhM7798+XKmtqioKKNkyZLm8qlTpwwXFxejWbNmRnp6utn+3//+15BkdOzY0Wzr37+/Icn4/vvvzbaLFy8aoaGhRokSJYy0tDTDMAyjZcuWRsWKFW855xtZv369IckoWrSokZSUZLYvWrTIkGRMnz7dMAzDSElJMQIDA41KlSoZf/31l9lv6dKlhiRj1KhRZlvHjh0NScawYcOyVMPo0aMNScYTTzxh196rVy9DkrFnzx6zrXjx4nafz5UrV8zPIENcXJzh6upqjBs3LtM8w8LCjKtXr5rt06dPNyQZe/fuNQzj+v5UpkwZIyoqyu53c/nyZSM0NNR4/PHHzbY73Q8AR+OUGZAHNWzYUAEBAQoJCVGbNm3k6empJUuWqFixYpKunxpZt26dnn76aV28eFFnzpzRmTNndPbsWUVFRenQoUPmqRtfX1/t379fhw4dyvV5ZBxNkaTExESdOXNGdevW1dGjR5WYmChJWrNmjVJSUtS3b1/ZbDazf//+/TONt3z5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PfnkkwoPD1dwcLCOHTt229vz9vbWM888o/fee08LFy7UF198oXPnzpnrt23bZtd/27ZtCgsLkySFhYVpz549unTpkl1dTk5OdkdtbuRG89yyZYtatmypF154QVWqVFHJkiX166+/mutLlSql/Pnza/v27Wbb+fPn7fqEhYXp2rVrdn3Onj2rgwcPqkKFCln5SLKNQAQAQA4pUaKEtm/frmPHjunMmTPm0Zx/KlOmjL788kvFxMRoz549ev7552/a92amTJmiTz/9VAcOHNCvv/6qxYsXKzg4WL6+vmafxYsX64MPPtCvv/6q0aNHa8eOHeY1Su3atZObm5s6duyoffv2af369erbt6/at29vXj90q3lu2rRJf/zxh86cOWPOafXq1frhhx8UGxur//znP0pISDDf4+Xlpa5du2rw4MFat26d9u3bp06dOsnJ6f9HkTJlyqhly5bq3r27Nm/erD179uiFF15Q0aJF1bJly9v6fG4XgQgAgBwyaNAgOTs7q0KFCgoICMh0TVCGKVOmqGDBgnrkkUfUokULRUVFqWrVqre1rQIFCmjSpEmqVq2aHn74YR07dkzLly+3Cxhjx47VZ599psqVK+vDDz/Up59+ah5p8fDw0MqVK3Xu3Dk9/PDDatOmjRo0aKA333zzX7c9btw4HTt2TKVKlVJAQIAkacSIEapataqioqJUr149BQcHq1WrVnbve/311/Xoo4+qRYsWatiwoWrXrq2IiAi7PnPnzlVERISaN2+uyMhIGYah5cuX39E32WeFzTAM465u4T6QlJQkHx8fJSYmytvbO9vjcJfZddxlBuBedeXKFcXFxSk0NFRubm6OLueWbDabvvrqq0yh5H5zq9/J7fz95ggRAACwPAIRAACwPB7MCADAfYgrYm4PR4gAAIDlEYgAAIDlEYgAAIDlEYgAAIDlEYgAAIDlOTQQRUdH6+GHH1aBAgUUGBioVq1a2X3DriTVq1dPNpvN7vXiiy/a9Tl+/LiaNWsmDw8PBQYGavDgwbp27Zpdnw0bNqhq1apydXVV6dKlNW/evLs9PQAAcI9waCDauHGjevfurW3btmn16tVKTU1Vo0aN7L5oTpK6d++ukydPmq9JkyaZ69LS0tSsWTOlpKTohx9+0Pz58zVv3jyNGjXK7BMXF6dmzZqpfv36iomJUf/+/dWtWzetXLky1+YK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m1auXJmr8wUAAHmTzTAMw9FFZDh9+rQCAwO1ceNG1alTR4mJiQoICNAnn3yiNm3aSJIOHDigsLAwbd26VTVr1tR3332n5s2b688//1RQUJAkafbs2Ro6dKhOnz4tFxcXDR06VMuWLdO+ffvMbT377LO6cOGCVqxY8a91JSUlycfHR4mJifL29s72/AaPnZzt995PXh/9sqNLAABYwO38/c5T1xAlJiZKkvz8/CRJu3btUmpqqho2bGj2KV++vB544AFt3bpVkrR161aFh4ebYUiSoqKilJSUpP3795t9/j5GRp+MMf7p6tWrSkpKsnsBAID7V54JROnp6erfv79q1aqlSpUqSZLi4+Pl4uIiX19fu75BQUGKj483+/w9DGWsz1h3qz5JSUn666+/MtUSHR0tHx8f8xUSEpIjcwQAAHlTnglEvXv31r59+/TZZ585uhQNHz5ciYmJ5uvEiROOLgkAANxF+RxdgCT16dNHS5cu1aZNm1SsWDGzPTg4WCkpKbpw4YLdUaKEhAQFBwebfXbs2GE3XsZdaH/v88870xISEuTt7S13d/dM9bi6usrV1TVH5gYAAPI+hx4hMgxDffr00VdffaV169YpNDTUbn1ERITy58+vtWvXmm0HDx7U8ePHFRkZKUmKjIzU3r17derUKbPP6tWr5e3trQoVKph9/j5GRp+MMQAAgLU59AhR79699cknn+ibb75RgQIFzGt+fHx85O7uLh8fH3Xt2lUDBw6Un5+fvL291bdvX0VGRqpmzZqSpEaNGqlChQpq3769Jk2apPj4eI0YMUK9e/c2j/K8+OKLevPNNzVkyBB16dJF69at06JFi7Rs2TKHzR0AAOQdDj1C9PbbbysxMVH16tVT4cKFzdfChQvNPlOnTlXz5s3VunVr1alTR8HBwfryyy/N9c7Ozlq6dKmcnZ0VGRmpF154QR06dNC4cePMPqGhoVq2bJlWr16tKlWqaPLkyZozZ46ioqJydb4AACBvylPPIcqreA5RzuI5RACA3HA7f7/zxEXVsJaEQR0dXUKeEPTGfEeXAAD4P3nmtnsAAABHIRABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLy5fVjjNmzMjyoP369ctWMQAAAI6Q5UA0depUu+XTp0/r8uXL8vX1lSRduHBBHh4eCgwMJBABAIB7SpZPmcXFxZmvCRMm6MEHH1RsbKzOnTunc+fOKTY2VlWrVtX48ePvZr0AAAA5LlvXEI0cOVIzZ85UuXLlzLZy5cpp6tSpGjFiRI4VBwAAkBuyFYhOnjypa9euZWpPS0tTQkLCHRcFAACQm7IViBo0aKD//Oc/2r17t9m2a9cu9ezZUw0bNsyx4gAAAHJDtgLRBx98oODgYFWrVk2urq5ydXVV9erVFRQUpDlz5uR0jQAAAHdVlu8y+7uAgAAtX75cv/76qw4cOCBJKl++vMqWLZujxQEAAOSGO3owY9myZfXEE0/oiSeeyFYY2rRpk1q0aKEiRYrIZrPp66+/tlvfqVMn2Ww2u1fjxo3t+pw7d07t2rWTt7e3fH191bVrVyUnJ9v1+fnnn/Xoo4/Kzc1NISEhmjRp0m3XCgAA7l/ZOkIkSb///ruWLFmi48ePKyUlxW7dlClTsjTGpUuXVKVKFXXp0kVPPfXUDfs0btxYc+fONZddXV3t1rdr104nT57U6tWrlZqaqs6dO6tHjx765JNPJElJSUlq1KiRGjZsqNmzZ2vv3r3q0qWLfH191aNHj9uZMgAAuE9lKxCtXbtWTzzxhEqWLKkDBw6oUqVKOnbsmAzDUNWqVbM8TpMmTdSkSZNb9nF1dVVwcPAN18XGxmrFihXauXOnqlWrJkmaOXOmmjZtqjfeeENFihTRggULlJKSog8++EAuLi6qWLGiYmJiNGXKFAIRAACQlM1TZsOHD9egQYO0d+9eubm56YsvvtCJEydUt25dtW3bNkcL3LBhgwIDA1WuXDn17NlTZ8+eNddt3bpVvr6+ZhiSpIYNG8rJyUnbt283+9SpU0cuLi5mn6ioKB08eFDnz5+/4TavXr2qpKQkuxcAALh/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+f03G+PvbRmBKmPc5ORktWjRQhMnTsw0VuHChW9r2wAyIxAByBHbt2+3W864PuefAWXXrl1KT0/X5MmT5eR0/SD1okWLbmtbQUFBKlKkiI4ePap27drdsI+Li4skZTpCtWXLFr311ltq2rSpJOnEiRM5emFyWFiYvvjiCxmGYYaaLVu2qECBAipWrFi2x61ataq++OILlShRQvny8U83kNM4ZQYgRxw/flwDBw7UwYMH9emnn2rmzJl66aWXMvUrXbq0UlNTNXPmTB09elQfffSRZs+efdvbGzt2rKKjozVjxgz9+uuv2rt3r+bOnaspU6ZIkgIDA+Xu7m5efJyYmChJKlOmjD766CPFxsZq+/btateundzd3e9s8n/Tq1cvnThxQn379tWBAwf0zTffaPTo0Ro4cKAZALOjd+/eOnfunJ577jnt3LlTR44c0cqVK9W5c+cbnpYEcHsIRAByRIcOHfTXX3+pevXq6t27t1566SX16NEjU78qVapoypQpmjhxoipVqqQFCxYoOjr6trfXrVs3zZkzR3PnzlV4eLjq1q2refPmmbfb58uXTzNmzNA777yjIkWKqGXLlpKk999/X+fPn1fVqlXVvn179evXT4GBgXc2+b8pWrSoli9frh07dqhKlSp68cUX1bVrV40YMeKOxi1SpIi2bNmitLQ0NWrUSOHh4erfv798fX3vKGgBuM5mGDd5UAgAZFG9evX04IMP3jdfzwHAevjfCgAAYHkEIgD4PwsWLLC7rf3vr4oVKzq6PAB3EafMAOD/XLx4UQkJCTdclz9/fhUvXjyXKwKQWwhEAADA8jhlBgAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALI9ABAAALO//Ac8i+ZlcberzAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.barplot(data = transportados_por_planeta, x = 'planeta_home', y = 'cantidad', hue = 'transportado', palette = {True:'Tomato', False:'SlateGrey'}).set(title = 'Resultados por planeta')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vK9AqeGvLcFE"
      },
      "source": [
        "Cuantos llegaron a c/ destino"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 642,
      "metadata": {
        "id": "wj7VlhtnKe9b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0e7bbf4c-17c3-49f2-d361-a13ecb7c807e"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['TRAPPIST-1e', 'PSO J318.5-22', '55 Cancri e', nan], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 642
        }
      ],
      "source": [
        "my_train.Destination.unique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 643,
      "metadata": {
        "id": "IAYUnaV8Leva"
      },
      "outputs": [],
      "source": [
        "salvados_por_destino_y_llegada = my_train.groupby(['HomePlanet','Destination', 'Transported']).agg({'PassengerId':['count']})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 644,
      "metadata": {
        "id": "qOt_VxpZMTQK"
      },
      "outputs": [],
      "source": [
        "salvados_por_destino_y_llegada = salvados_por_destino_y_llegada.unstack()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 645,
      "metadata": {
        "id": "-Acg_ggkMbmh"
      },
      "outputs": [],
      "source": [
        "salvados_por_destino_y_llegada = salvados_por_destino_y_llegada.reset_index()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 646,
      "metadata": {
        "id": "tj10OOd1MhzR"
      },
      "outputs": [],
      "source": [
        "salvados_por_destino_y_llegada.columns = ['origen', 'destino', 'llegaron', 'no llegaron']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 647,
      "metadata": {
        "id": "3FefhuswNRMs"
      },
      "outputs": [],
      "source": [
        "salvados_por_destino_y_llegada['porcentaje_salvados']  = (salvados_por_destino_y_llegada['llegaron']*100 /\n",
        " ( salvados_por_destino_y_llegada['llegaron'] + salvados_por_destino_y_llegada['no llegaron'] ) ).round(2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 648,
      "metadata": {
        "id": "XwYBmHEjNn-7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 332
        },
        "outputId": "18a52141-3e72-4e9e-80bc-05fbda43cca2"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   origen        destino  llegaron  no llegaron  porcentaje_salvados\n",
              "0   Earth    55 Cancri e       342          348                49.57\n",
              "1   Earth  PSO J318.5-22       357          355                50.14\n",
              "2   Earth    TRAPPIST-1e      1894         1207                61.08\n",
              "3  Europa    55 Cancri e       275          611                31.04\n",
              "4  Europa  PSO J318.5-22         5           14                26.32\n",
              "5  Europa    TRAPPIST-1e       434          755                36.50\n",
              "6    Mars    55 Cancri e        75          118                38.86\n",
              "7    Mars  PSO J318.5-22        27           22                55.10\n",
              "8    Mars    TRAPPIST-1e       720          755                48.81"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ed308081-f243-4e82-9c93-4fd339cefe1b\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>origen</th>\n",
              "      <th>destino</th>\n",
              "      <th>llegaron</th>\n",
              "      <th>no llegaron</th>\n",
              "      <th>porcentaje_salvados</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Earth</td>\n",
              "      <td>55 Cancri e</td>\n",
              "      <td>342</td>\n",
              "      <td>348</td>\n",
              "      <td>49.57</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Earth</td>\n",
              "      <td>PSO J318.5-22</td>\n",
              "      <td>357</td>\n",
              "      <td>355</td>\n",
              "      <td>50.14</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Earth</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>1894</td>\n",
              "      <td>1207</td>\n",
              "      <td>61.08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Europa</td>\n",
              "      <td>55 Cancri e</td>\n",
              "      <td>275</td>\n",
              "      <td>611</td>\n",
              "      <td>31.04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Europa</td>\n",
              "      <td>PSO J318.5-22</td>\n",
              "      <td>5</td>\n",
              "      <td>14</td>\n",
              "      <td>26.32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Europa</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>434</td>\n",
              "      <td>755</td>\n",
              "      <td>36.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Mars</td>\n",
              "      <td>55 Cancri e</td>\n",
              "      <td>75</td>\n",
              "      <td>118</td>\n",
              "      <td>38.86</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>Mars</td>\n",
              "      <td>PSO J318.5-22</td>\n",
              "      <td>27</td>\n",
              "      <td>22</td>\n",
              "      <td>55.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Mars</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>720</td>\n",
              "      <td>755</td>\n",
              "      <td>48.81</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ed308081-f243-4e82-9c93-4fd339cefe1b')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-ed308081-f243-4e82-9c93-4fd339cefe1b button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-ed308081-f243-4e82-9c93-4fd339cefe1b');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-84728fac-8e8c-43c4-97f1-6bc4a63daf93\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-84728fac-8e8c-43c4-97f1-6bc4a63daf93')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-84728fac-8e8c-43c4-97f1-6bc4a63daf93 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 648
        }
      ],
      "source": [
        "salvados_por_destino_y_llegada"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 649,
      "metadata": {
        "id": "4FDnev8ROCsX"
      },
      "outputs": [],
      "source": [
        "matriz = salvados_por_destino_y_llegada.pivot_table(values = 'porcentaje_salvados' , index = 'origen' , columns = 'destino')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 650,
      "metadata": {
        "id": "n2UWPiQqOVZ7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 476
        },
        "outputId": "8ab78c76-7e84-4706-8ab2-8d7cf8fc3f0e"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "cmap = sns.color_palette(\"Reds_r\", as_cmap=True )\n",
        "ax = sns.heatmap(matriz,square=True,cmap=cmap, cbar_kws = {'label': 'porcentaje (%)'}, linewidth = .5, vmax = 100, vmin = 0, annot = True)\n",
        "### Labels ###\n",
        "plt.title(\"Porcentaje de salvados por origen y destino\")\n",
        "plt.xlabel('origen', fontsize = 12)\n",
        "plt.ylabel('destino', fontsize = 12)\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 651,
      "metadata": {
        "id": "WSa5ZOBcCbyQ"
      },
      "outputs": [],
      "source": [
        "#my_train.groupby('Age').transform()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LZomLGi0SWS6"
      },
      "source": [
        "## Imputacion"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 652,
      "metadata": {
        "id": "0VtZkRHCQRJR",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "outputId": "da478fc5-dea6-4666-eb23-03e1f566a58d"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  PassengerId HomePlanet CryoSleep  Cabin  Destination   Age    VIP  \\\n",
              "0     0001_01     Europa     False  B/0/P  TRAPPIST-1e  39.0  False   \n",
              "1     0002_01      Earth     False  F/0/S  TRAPPIST-1e  24.0  False   \n",
              "2     0003_01     Europa     False  A/0/S  TRAPPIST-1e  58.0   True   \n",
              "3     0003_02     Europa     False  A/0/S  TRAPPIST-1e  33.0  False   \n",
              "4     0004_01      Earth     False  F/1/S  TRAPPIST-1e  16.0  False   \n",
              "\n",
              "   RoomService  FoodCourt  ShoppingMall     Spa  VRDeck               Name  \\\n",
              "0          0.0        0.0           0.0     0.0     0.0    Maham Ofracculy   \n",
              "1        109.0        9.0          25.0   549.0    44.0       Juanna Vines   \n",
              "2         43.0     3576.0           0.0  6715.0    49.0      Altark Susent   \n",
              "3          0.0     1283.0         371.0  3329.0   193.0       Solam Susent   \n",
              "4        303.0       70.0         151.0   565.0     2.0  Willy Santantines   \n",
              "\n",
              "   Transported  \n",
              "0        False  \n",
              "1         True  \n",
              "2        False  \n",
              "3        False  \n",
              "4         True  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-1b0bd87c-1dff-4e86-bdf5-56a91a598f22\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>HomePlanet</th>\n",
              "      <th>CryoSleep</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Destination</th>\n",
              "      <th>Age</th>\n",
              "      <th>VIP</th>\n",
              "      <th>RoomService</th>\n",
              "      <th>FoodCourt</th>\n",
              "      <th>ShoppingMall</th>\n",
              "      <th>Spa</th>\n",
              "      <th>VRDeck</th>\n",
              "      <th>Name</th>\n",
              "      <th>Transported</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0001_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>B/0/P</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>39.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Maham Ofracculy</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0002_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>F/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>24.0</td>\n",
              "      <td>False</td>\n",
              "      <td>109.0</td>\n",
              "      <td>9.0</td>\n",
              "      <td>25.0</td>\n",
              "      <td>549.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>Juanna Vines</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0003_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>58.0</td>\n",
              "      <td>True</td>\n",
              "      <td>43.0</td>\n",
              "      <td>3576.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>6715.0</td>\n",
              "      <td>49.0</td>\n",
              "      <td>Altark Susent</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0003_02</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>33.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1283.0</td>\n",
              "      <td>371.0</td>\n",
              "      <td>3329.0</td>\n",
              "      <td>193.0</td>\n",
              "      <td>Solam Susent</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0004_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>F/1/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>16.0</td>\n",
              "      <td>False</td>\n",
              "      <td>303.0</td>\n",
              "      <td>70.0</td>\n",
              "      <td>151.0</td>\n",
              "      <td>565.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>Willy Santantines</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-1b0bd87c-1dff-4e86-bdf5-56a91a598f22')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-1b0bd87c-1dff-4e86-bdf5-56a91a598f22 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-1b0bd87c-1dff-4e86-bdf5-56a91a598f22');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-08c11697-ae12-4502-8524-11dba9b2d260\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-08c11697-ae12-4502-8524-11dba9b2d260')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-08c11697-ae12-4502-8524-11dba9b2d260 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 652
        }
      ],
      "source": [
        "my_train.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Fit-dOoN7-Be"
      },
      "source": [
        "Hay un unico valor de Id"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 653,
      "metadata": {
        "id": "_umQIc6c7zP5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1e312a1b-0e1d-4ca3-95ec-999e7bd2a573"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 653
        }
      ],
      "source": [
        "my_train.PassengerId.nunique() == len(my_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 654,
      "metadata": {
        "id": "d_BWcP-gSZw0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "08829375-3f48-49c2-cb7d-5039c4948e6c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 8693 entries, 0 to 8692\n",
            "Data columns (total 14 columns):\n",
            " #   Column        Non-Null Count  Dtype  \n",
            "---  ------        --------------  -----  \n",
            " 0   PassengerId   8693 non-null   object \n",
            " 1   HomePlanet    8492 non-null   object \n",
            " 2   CryoSleep     8476 non-null   object \n",
            " 3   Cabin         8494 non-null   object \n",
            " 4   Destination   8511 non-null   object \n",
            " 5   Age           8514 non-null   float64\n",
            " 6   VIP           8490 non-null   object \n",
            " 7   RoomService   8512 non-null   float64\n",
            " 8   FoodCourt     8510 non-null   float64\n",
            " 9   ShoppingMall  8485 non-null   float64\n",
            " 10  Spa           8510 non-null   float64\n",
            " 11  VRDeck        8505 non-null   float64\n",
            " 12  Name          8493 non-null   object \n",
            " 13  Transported   8693 non-null   bool   \n",
            "dtypes: bool(1), float64(6), object(7)\n",
            "memory usage: 891.5+ KB\n"
          ]
        }
      ],
      "source": [
        "my_train.info()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TPkqd1G-URFf"
      },
      "source": [
        "Porcentaje de valores faltantes por feature"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 655,
      "metadata": {
        "id": "oTz4Y3DZ9pPr",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "acb3bbc2-3fc2-4145-fd57-6b1f36c95eba"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "PassengerId       0\n",
              "HomePlanet      201\n",
              "CryoSleep       217\n",
              "Cabin           199\n",
              "Destination     182\n",
              "Age             179\n",
              "VIP             203\n",
              "RoomService     181\n",
              "FoodCourt       183\n",
              "ShoppingMall    208\n",
              "Spa             183\n",
              "VRDeck          188\n",
              "Name            200\n",
              "Transported       0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 655
        }
      ],
      "source": [
        "my_train.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 656,
      "metadata": {
        "id": "WMEdLAG7SkD3"
      },
      "outputs": [],
      "source": [
        "nan_perc_dict = (( len(my_train) - my_train.count() )*100 / len(my_train)).nlargest(len(my_train.columns)).to_dict()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 657,
      "metadata": {
        "id": "w6Igj_DN7feF"
      },
      "outputs": [],
      "source": [
        "porcentaje_valores_faltantes = pd.DataFrame(nan_perc_dict.items())\n",
        "porcentaje_valores_faltantes.columns = ['Columna', 'Valores faltantes']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 658,
      "metadata": {
        "id": "ywKCrame9XdM",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 551
        },
        "outputId": "0a5c9c91-4841-4b2e-d3bf-1b1041df7797"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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UbrnxtHREefOncvRvmPHDri5uSn1XEIIBAcH4++//8bevXvh6Pjx5a7r1KmDyMhIhbbdu3ejTp06Sh2biIiItJPSPTehoaHo27cvXr16BSEETp48ib/++guTJk3C0qVLlXquvn37Ys2aNdi6dSvMzMzk42YsLCxgbGwMAAgMDETp0qUxadIkAED//v3RsGFDTJs2Dc2bN8fatWtx+vRpLF68WNkvhYiIiLSQ0sVNz549YWxsjF9++QUvXrxAp06dYGtri1mzZqFDhw5KPdeCBQsAAF5eXgrtK1asQNeuXQEA8fHx0NH5XwdT3bp1sWbNGvzyyy/4+eef4erqii1btnxwEDIRERF9OZQubgCgc+fO6Ny5M168eIHU1FRYW1sX6OBCiI/us3///hxtAQEBCAgIKNAxiYiISLspPeamcePGSE5OBgAUKVJEXtikpKSgcePGhRqOiIiISFlKFzf79+9HRkZGjvZXr17h0KFDhRKKiIiIqKDyfVrq/Pnz8v9funRJYdG8zMxM7NixA6VLly7cdERERERKyndxU6VKFchkMshkslxPPxkbG2POnDmFGo6IiIhIWfkubm7dugUhBJycnHDy5EmUKFFCvs3AwADW1tYKKxYTERERqUO+ixt7e3sAb68BRURERKSpCjQV/Nq1a9i3bx8ePHiQo9gZPXp0oQQjIiIiKgili5slS5bgxx9/RPHixWFjYwOZTCbfJpPJWNwQERGRWild3EyYMAETJ07EsGHDVJGHiIiI6JMovc7N06dPuTowERERaSyli5uAgADs2rVLFVmIiIiIPpnSp6VcXFwwatQoHD9+HJ6entDX11fYHhISUmjhiIiIiJSldHGzePFimJqa4sCBAzhw4IDCNplMxuKGiIiI1Erp4ubWrVuqyEFERERUKJQec0NERESkyQq0iN+dO3cQERGB+Pj4HFcInz59eqEEIyIiIioIpYubyMhI+Pv7w8nJCZcvX4aHhwfi4uIghEC1atVUkZGIiIgo35Q+LTVixAgMHjwYMTExMDIywqZNm5CQkICGDRty/RsiIiJSO6WLm9jYWAQGBgIA9PT08PLlS5iamiIsLAyTJ08u9IBEREREylC6uDExMZGPsylVqhRu3Lgh3/bo0aPCS0ZERERUAEqPualduzYOHz4MNzc3+Pn5YdCgQYiJicHmzZtRu3ZtVWQkIiIiyjeli5vp06cjNTUVADBu3DikpqZi3bp1cHV15UwpIiIiUjulixsnJyf5/01MTLBw4cJCDURERET0KZQec+Pk5ITHjx/naE9OTlYofIiIiIjUQeniJi4uDpmZmTna09PTcffu3UIJRURERFRQ+T4tFRERIf//zp07YWFhIb+fmZmJyMhIODg4FGo4IiIiImXlu7hp1aoVgLdX/g4KClLYpq+vDwcHB0ybNq1QwxEREREpK9/FTVZWFgDA0dERp06dQvHixVUWioiIiKiglJ4tdevWLVXkICIiIioU+SpuZs+ene8nDAkJKXAYIiIiok+Vr+JmxowZ+XoymUzG4oaIiIjUKl/FDU9FERER0edC6XVuiIiIiDSZ0gOKAeDOnTuIiIhAfHy8/Arh2Xh9KSIiIlInpYubyMhI+Pv7w8nJCZcvX4aHhwfi4uIghEC1atVUkZGIiIgo35Q+LTVixAgMHjwYMTExMDIywqZNm5CQkICGDRsiICBAFRmJiIiI8k3p4iY2NhaBgYEAAD09Pbx8+RKmpqYICwvD5MmTCz0gERERkTKULm5MTEzk42xKlSqFGzduyLc9evSo8JIRERERFYDSY25q166Nw4cPw83NDX5+fhg0aBBiYmKwefNm1K5dWxUZiYiIiPJN6eJm+vTpSE1NBQCMGzcOqampWLduHVxdXTlTioiIiNQu35df+OGHH2BkZAQ9PT14enoCeHuKauHChSoNSERERKSMfI25CQ0NRUpKCoC3VwV/+PChSkMRERERFVS+em5sbW2xadMm+Pn5QQiBO3fu4NWrV7nuW7Zs2UINSERERKSMfBU3v/zyC/r164fg4GDIZDLUrFkzxz5CCMhkMmRmZhZ6SCIiIqL8yldx88MPP6Bjx464ffs2KlWqhD179qBYsWKqzkZERESktHzPljIzM4OHhwdWrFiBevXqwdDQUJW5iIiIiApE6angQUFBqshBREREVCiUXqGYiIiISJOxuCEiIiKtwuKGiIiItMonFzeZmZk4d+4cnj59Whh5iIiIiD6J0sXNgAEDsGzZMgBvC5uGDRuiWrVqsLOzw/79+ws7HxEREZFSlC5uNm7ciMqVKwMAtm3bhlu3buHy5csYOHAgRo4cWegBiYiIiJShdHHz6NEj2NjYAAC2b9+OgIAAlCtXDt27d0dMTEyhByQiIiJShtLFTcmSJXHp0iVkZmZix44d+OabbwAAL168gK6ubqEHJCIiIlKG0ov4devWDe3atUOpUqUgk8ng4+MDADhx4gQqVKhQ6AGJiIiIlKF0cTN27Fh4eHggISEBAQEB8ssw6OrqYvjw4YUekIiIiEgZShc3APDdd98BAF69eiVv42UZiIiISBMoPeYmMzMT48ePR+nSpWFqaoqbN28CAEaNGiWfIk5ERESkLkoXNxMnTkR4eDimTJkCAwMDebuHhweWLl1aqOGIiIiIlKV0cbNq1SosXrwYnTt3VpgdVblyZVy+fFmp5zp48CBatGgBW1tbyGQybNmy5YP779+/HzKZLMft/v37yn4ZREREpKWULm7u3r0LFxeXHO1ZWVl4/fq1Us+VlpaGypUrY968eUo97sqVK0hMTJTfrK2tlXo8ERERaS+lBxRXrFgRhw4dgr29vUL7xo0bUbVqVaWey9fXF76+vspGgLW1NSwtLZV+HBEREWk/pYub0aNHIygoCHfv3kVWVhY2b96MK1euYNWqVfjnn39UkTGHKlWqID09HR4eHhg7dizq1auX577p6elIT0+X309JSZEiIhEREamJ0qelWrZsiW3btmHPnj0wMTHB6NGjERsbi23btslXK1aVUqVKYeHChdi0aRM2bdoEOzs7eHl5ISoqKs/HTJo0CRYWFvKbnZ2dSjMSERGReinVc/PmzRv8+uuv6N69O3bv3q2qTHkqX748ypcvL79ft25d3LhxAzNmzMDq1atzfcyIESMQGhoqv5+SksICh4iISIsp1XOjp6eHKVOm4M2bN6rKo7RatWrh+vXreW43NDSEubm5wo2IiIi0l9Knpby9vXHgwAFVZCmQc+fOoVSpUuqOQURERBpC6QHFvr6+GD58OGJiYlC9enWYmJgobPf398/3c6Wmpir0uty6dQvnzp1D0aJFUbZsWYwYMQJ3797FqlWrAAAzZ86Eo6Mj3N3d8erVKyxduhR79+7Frl27lP0yiIiISEspXdz89NNPAIDp06fn2CaTyZCZmZnv5zp9+jQaNWokv589NiYoKAjh4eFITExEfHy8fHtGRgYGDRqEu3fvokiRIqhUqRL27Nmj8BxERET0ZVO6uMnKyiq0g3t5eUEIkef28PBwhftDhw7F0KFDC+34REREpH2UHnNDREREpMkKVNwcOHAALVq0gIuLC1xcXODv749Dhw4VdjYiIiIipSld3Pzxxx/w8fFBkSJFEBISgpCQEBgbG8Pb2xtr1qxRRUYiIiKifFN6zM3EiRMxZcoUDBw4UN4WEhKC6dOnY/z48ejUqVOhBiQiIiJShtI9Nzdv3kSLFi1ytPv7++PWrVuFEoqIiIiooJQubuzs7BAZGZmjfc+ePbysAREREamd0qelBg0ahJCQEJw7dw5169YFABw5cgTh4eGYNWtWoQckIiIiUobSxc2PP/4IGxsbTJs2DevXrwcAuLm5Yd26dWjZsmWhByQiIiJShtLFDQC0bt0arVu3LuwsRERERJ+Mi/gRERGRVslXz42VlRVkMlm+nvDJkyefFIiIiIjoU+SruJk5c6aKYxAREREVjnwVN0FBQarOQURERFQoCjSgONurV6+QkZGh0GZubv5JgYiIiIg+hdIDitPS0hAcHAxra2uYmJjAyspK4UZERESkTkoXN0OHDsXevXuxYMECGBoaYunSpRg3bhxsbW2xatUqVWQkIiIiyjelT0tt27YNq1atgpeXF7p164b69evDxcUF9vb2+PPPP9G5c2dV5CQiIiLKF6V7bp48eQInJycAb8fXZE/9/vrrr3Hw4MHCTUdERESkJKWLGycnJ/nVvytUqCC/BMO2bdtgaWlZqOGIiIiIlKV0cdOtWzdER0cDAIYPH4558+bByMgIAwcOxJAhQwo9IBEREZEylB5zM3DgQPn/fXx8cPnyZZw5cwYuLi6oVKlSoYYjIiIiUpbSxU1CQgLs7Ozk9+3t7WFvb1+ooYiIiIgKSunTUg4ODmjYsCGWLFmCp0+fqiITERERUYEpXdycPn0atWrVQlhYGEqVKoVWrVph48aNSE9PV0U+IiIiIqUoXdxUrVoVU6dORXx8PP777z+UKFECP/zwA0qWLInu3burIiMRERFRvild3GSTyWRo1KgRlixZgj179sDR0RErV64szGxERERESitwcXPnzh1MmTIFVapUQa1atWBqaop58+YVZjYiIiIipSk9W2rRokVYs2YNjhw5ggoVKqBz587YunUrZ0wRERGRRlC6uJkwYQI6duyI2bNno3LlyqrIRERERFRgShc38fHxkMlkqshCRERE9MmUHnPDwoaIiIg0WYEHFBMRERFpIhY3REREpFVY3BAREZFWKVBx8+bNG+zZsweLFi3C8+fPAQD37t1DampqoYYjIiIi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fPnyAN5eTNPOzg7//vsvnJ2dCz0kERERUX4pPVsqJCQEzs7OSEhIQFRUFKKiouQX0wwJCVFFRiIiIqJ8U7rn5sCBAzh+/DiKFi0qbytWrBh+++031KtXr1DDERERESlL6Z4bQ0NDPH/+PEd7amoqDAwMCiUUERERUUEpXdx8++23+OGHH3DixAkIISCEwPHjx9GnTx/4+/urIiMRERFRvild3MyePRvOzs6oU6cOjIyMYGRkhHr16sHFxQWzZs1SRUYiIiKifFN6zI2lpSW2bt2K69evy6eCu7m5wcXFpdDDERERESkr38VNVlYWpk6dioiICGRkZMDb2xtjxozJcfkFIiIiInXK92mpiRMn4ueff4apqSlKly6NWbNmoW/fvqrMRkRERKS0fBc3q1atwvz587Fz505s2bIF27Ztw59//omsrCxV5iMiIiJSSr6Lm/j4ePj5+cnv+/j4QCaT4d69eyoJRkRERFQQ+S5u3rx5AyMjI4U2fX19vH79utBDERERERVUvgcUCyHQtWtXGBoayttevXqFPn36wMTERN62efPmwk1IREREpIR8FzdBQUE52rp06VKoYYiIiIg+Vb6LmxUrVqgyBxEREVGhUHqFYiIiIiJNphHFzbx58+Dg4AAjIyN89dVXOHnyZJ77hoeHQyaTKdzeH+hMREREXy61Fzfr1q1DaGgoxowZg6ioKFSuXBlNmzbFgwcP8nyMubk5EhMT5bfbt29LmJiIiIg0mdqLm+nTp6NXr17o1q0bKlasiIULF6JIkSJYvnx5no+RyWSwsbGR30qWLClhYiIiItJkai1uMjIycObMGfj4+MjbdHR04OPjg2PHjuX5uNTUVNjb28POzg4tW7bExYsX89w3PT0dKSkpCjciIiLSXmotbh49eoTMzMwcPS8lS5bE/fv3c31M+fLlsXz5cmzduhV//PEHsrKyULduXdy5cyfX/SdNmgQLCwv5zc7OrtC/DiIiItIcaj8tpaw6deogMDAQVapUQcOGDbF582aUKFECixYtynX/ESNG4NmzZ/JbQkKCxImJiIhISvle50YVihcvDl1dXSQlJSm0JyUlwcbGJl/Poa+vj6pVq+L69eu5bjc0NFRYVZmIiIi0m1p7bgwMDFC9enVERkbK27KyshAZGYk6derk6zkyMzMRExODUqVKqSomERERfUbU2nMDAKGhoQgKCkKNGjVQq1YtzJw5E2lpaejWrRsAIDAwEKVLl8akSZMAAGFhYahduzZcXFyQnJyMqVOn4vbt2+jZs6c6vwwiIiLSEGovbtq3b4+HDx9i9OjRuH//PqpUqYIdO3bIBxnHx8dDR+d/HUxPnz5Fr169cP/+fVhZWaF69eo4evQoKlasqK4vgYiIiDSI2osbAAgODkZwcHCu2/bv369wf8aMGZgxY4YEqYiIiOhz9NnNliIiIiL6EBY3REREpFVY3BAREZFWYXFDREREWoXFDREREWkVFjdERESkVVjcEBERkVZhcUNERERahcUNERERaRUWN0RERKRVWNwQERGRVmFxQ0RERFqFxQ0RERFpFRY3REREpFVY3BAREZFWYXFDREREWoXFDREREWkVFjdERESkVVjcEBERkVZhcUNERERahcUNERERaRUWN0RERKRVWNwQERGRVmFxQ0RERFqFxQ0RERFpFRY3REREpFVY3BAREZFWYXFDREREWoXFDREREWkVFjdERESkVVjcEBERkVZhcUNERERahcUNERERaRUWN0RERKRVWNwQERGRVmFxQ0RERFqFxQ0RERFpFRY3REREpFVY3BAREZFWYXFDREREWoXFDREREWkVFjdERESkVVjcEBERkVZhcUNERERahcUNERERaRUWN0RERKRVWNwQERGRVmFxQ0RERFqFxQ0RERFpFRY3REREpFVY3BAREZFWYXFDREREWoXFDREREWkVFjdERESkVVjcEBERkVZhcUNERERahcUNERERaRUWN0RERKRVWNwQERGRVtGI4mbevHlwcHCAkZERvvrqK5w8efKD+2/YsAEVKlSAkZERPD09sX37domSEhERkaZTe3Gzbt06hIaGYsyYMYiKikLlypXRtGlTPHjwINf9jx49io4dO6JHjx44e/YsWrVqhVatWuHChQsSJyciIiJNpPbiZvr06ejVqxe6deuGihUrYuHChShSpAiWL1+e6/6zZs1Cs2bNMGTIELi5uWH8+PGoVq0a5s6dK3FyIiIi0kR66jx4RkYGzpw5gxEjRsjbdHR04OPjg2PHjuX6mGPHjiE0NFShrWnTptiyZUuu+6enpyM9PV1+/9mzZwCAlJQUedvztKyCfgkF8u6x3yd1FkCz8nwuWQDNyvMlZwE0K48mZQE0K8/nkgXQvDz0v++REOKj+6q1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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.barplot(data = porcentaje_valores_faltantes, x = 'Columna', y = 'Valores faltantes' , color = 'Gold').set(\n",
        "    ylabel = 'Porcentaje de valores faltantes', title='Porcentaje de valores faltantes por columna')\n",
        "plt.xticks(rotation=90)\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 659,
      "metadata": {
        "id": "HzdGObxDBk7a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "outputId": "7017638b-d7d8-410c-ac48-b36a216c959f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  PassengerId HomePlanet CryoSleep  Cabin  Destination   Age    VIP  \\\n",
              "0     0001_01     Europa     False  B/0/P  TRAPPIST-1e  39.0  False   \n",
              "1     0002_01      Earth     False  F/0/S  TRAPPIST-1e  24.0  False   \n",
              "2     0003_01     Europa     False  A/0/S  TRAPPIST-1e  58.0   True   \n",
              "3     0003_02     Europa     False  A/0/S  TRAPPIST-1e  33.0  False   \n",
              "4     0004_01      Earth     False  F/1/S  TRAPPIST-1e  16.0  False   \n",
              "\n",
              "   RoomService  FoodCourt  ShoppingMall     Spa  VRDeck               Name  \\\n",
              "0          0.0        0.0           0.0     0.0     0.0    Maham Ofracculy   \n",
              "1        109.0        9.0          25.0   549.0    44.0       Juanna Vines   \n",
              "2         43.0     3576.0           0.0  6715.0    49.0      Altark Susent   \n",
              "3          0.0     1283.0         371.0  3329.0   193.0       Solam Susent   \n",
              "4        303.0       70.0         151.0   565.0     2.0  Willy Santantines   \n",
              "\n",
              "   Transported  \n",
              "0        False  \n",
              "1         True  \n",
              "2        False  \n",
              "3        False  \n",
              "4         True  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ce1b4c5e-2ddb-4825-b44a-85c3d58187bc\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>HomePlanet</th>\n",
              "      <th>CryoSleep</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Destination</th>\n",
              "      <th>Age</th>\n",
              "      <th>VIP</th>\n",
              "      <th>RoomService</th>\n",
              "      <th>FoodCourt</th>\n",
              "      <th>ShoppingMall</th>\n",
              "      <th>Spa</th>\n",
              "      <th>VRDeck</th>\n",
              "      <th>Name</th>\n",
              "      <th>Transported</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0001_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>B/0/P</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>39.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Maham Ofracculy</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0002_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>F/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>24.0</td>\n",
              "      <td>False</td>\n",
              "      <td>109.0</td>\n",
              "      <td>9.0</td>\n",
              "      <td>25.0</td>\n",
              "      <td>549.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>Juanna Vines</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0003_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>58.0</td>\n",
              "      <td>True</td>\n",
              "      <td>43.0</td>\n",
              "      <td>3576.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>6715.0</td>\n",
              "      <td>49.0</td>\n",
              "      <td>Altark Susent</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0003_02</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>33.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1283.0</td>\n",
              "      <td>371.0</td>\n",
              "      <td>3329.0</td>\n",
              "      <td>193.0</td>\n",
              "      <td>Solam Susent</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0004_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>F/1/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>16.0</td>\n",
              "      <td>False</td>\n",
              "      <td>303.0</td>\n",
              "      <td>70.0</td>\n",
              "      <td>151.0</td>\n",
              "      <td>565.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>Willy Santantines</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ce1b4c5e-2ddb-4825-b44a-85c3d58187bc')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-ce1b4c5e-2ddb-4825-b44a-85c3d58187bc button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-ce1b4c5e-2ddb-4825-b44a-85c3d58187bc');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-1c8862a3-ea14-43bd-998c-b0da86d4c1d9\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-1c8862a3-ea14-43bd-998c-b0da86d4c1d9')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-1c8862a3-ea14-43bd-998c-b0da86d4c1d9 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 659
        }
      ],
      "source": [
        "my_train.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 660,
      "metadata": {
        "id": "3qlS4ynNEriT",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "outputId": "856ca364-e5d4-49e2-c430-9e69b75100d7"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     PassengerId HomePlanet CryoSleep     Cabin    Destination   Age    VIP  \\\n",
              "0        0001_01     Europa     False     B/0/P    TRAPPIST-1e  39.0  False   \n",
              "1        0002_01      Earth     False     F/0/S    TRAPPIST-1e  24.0  False   \n",
              "2        0003_01     Europa     False     A/0/S    TRAPPIST-1e  58.0   True   \n",
              "3        0003_02     Europa     False     A/0/S    TRAPPIST-1e  33.0  False   \n",
              "4        0004_01      Earth     False     F/1/S    TRAPPIST-1e  16.0  False   \n",
              "...          ...        ...       ...       ...            ...   ...    ...   \n",
              "8688     9276_01     Europa     False    A/98/P    55 Cancri e  41.0   True   \n",
              "8689     9278_01      Earth      True  G/1499/S  PSO J318.5-22  18.0  False   \n",
              "8690     9279_01      Earth     False  G/1500/S    TRAPPIST-1e  26.0  False   \n",
              "8691     9280_01     Europa     False   E/608/S    55 Cancri e  32.0  False   \n",
              "8692     9280_02     Europa     False   E/608/S    TRAPPIST-1e  44.0  False   \n",
              "\n",
              "      RoomService  FoodCourt  ShoppingMall     Spa  VRDeck               Name  \\\n",
              "0             0.0        0.0           0.0     0.0     0.0    Maham Ofracculy   \n",
              "1           109.0        9.0          25.0   549.0    44.0       Juanna Vines   \n",
              "2            43.0     3576.0           0.0  6715.0    49.0      Altark Susent   \n",
              "3             0.0     1283.0         371.0  3329.0   193.0       Solam Susent   \n",
              "4           303.0       70.0         151.0   565.0     2.0  Willy Santantines   \n",
              "...           ...        ...           ...     ...     ...                ...   \n",
              "8688          0.0     6819.0           0.0  1643.0    74.0  Gravior Noxnuther   \n",
              "8689          0.0        0.0           0.0     0.0     0.0    Kurta Mondalley   \n",
              "8690          0.0        0.0        1872.0     1.0     0.0       Fayey Connon   \n",
              "8691          0.0     1049.0           0.0   353.0  3235.0   Celeon Hontichre   \n",
              "8692        126.0     4688.0           0.0     0.0    12.0   Propsh Hontichre   \n",
              "\n",
              "      Transported  \n",
              "0           False  \n",
              "1            True  \n",
              "2           False  \n",
              "3           False  \n",
              "4            True  \n",
              "...           ...  \n",
              "8688        False  \n",
              "8689        False  \n",
              "8690         True  \n",
              "8691        False  \n",
              "8692         True  \n",
              "\n",
              "[8693 rows x 14 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-f4d02ffa-5b38-43a9-800a-76d67618075b\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>HomePlanet</th>\n",
              "      <th>CryoSleep</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Destination</th>\n",
              "      <th>Age</th>\n",
              "      <th>VIP</th>\n",
              "      <th>RoomService</th>\n",
              "      <th>FoodCourt</th>\n",
              "      <th>ShoppingMall</th>\n",
              "      <th>Spa</th>\n",
              "      <th>VRDeck</th>\n",
              "      <th>Name</th>\n",
              "      <th>Transported</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0001_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>B/0/P</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>39.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Maham Ofracculy</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0002_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>F/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>24.0</td>\n",
              "      <td>False</td>\n",
              "      <td>109.0</td>\n",
              "      <td>9.0</td>\n",
              "      <td>25.0</td>\n",
              "      <td>549.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>Juanna Vines</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0003_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>58.0</td>\n",
              "      <td>True</td>\n",
              "      <td>43.0</td>\n",
              "      <td>3576.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>6715.0</td>\n",
              "      <td>49.0</td>\n",
              "      <td>Altark Susent</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0003_02</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/0/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>33.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1283.0</td>\n",
              "      <td>371.0</td>\n",
              "      <td>3329.0</td>\n",
              "      <td>193.0</td>\n",
              "      <td>Solam Susent</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0004_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>F/1/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>16.0</td>\n",
              "      <td>False</td>\n",
              "      <td>303.0</td>\n",
              "      <td>70.0</td>\n",
              "      <td>151.0</td>\n",
              "      <td>565.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>Willy Santantines</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8688</th>\n",
              "      <td>9276_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>A/98/P</td>\n",
              "      <td>55 Cancri e</td>\n",
              "      <td>41.0</td>\n",
              "      <td>True</td>\n",
              "      <td>0.0</td>\n",
              "      <td>6819.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1643.0</td>\n",
              "      <td>74.0</td>\n",
              "      <td>Gravior Noxnuther</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8689</th>\n",
              "      <td>9278_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>True</td>\n",
              "      <td>G/1499/S</td>\n",
              "      <td>PSO J318.5-22</td>\n",
              "      <td>18.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Kurta Mondalley</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8690</th>\n",
              "      <td>9279_01</td>\n",
              "      <td>Earth</td>\n",
              "      <td>False</td>\n",
              "      <td>G/1500/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>26.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1872.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Fayey Connon</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8691</th>\n",
              "      <td>9280_01</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>E/608/S</td>\n",
              "      <td>55 Cancri e</td>\n",
              "      <td>32.0</td>\n",
              "      <td>False</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1049.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>353.0</td>\n",
              "      <td>3235.0</td>\n",
              "      <td>Celeon Hontichre</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8692</th>\n",
              "      <td>9280_02</td>\n",
              "      <td>Europa</td>\n",
              "      <td>False</td>\n",
              "      <td>E/608/S</td>\n",
              "      <td>TRAPPIST-1e</td>\n",
              "      <td>44.0</td>\n",
              "      <td>False</td>\n",
              "      <td>126.0</td>\n",
              "      <td>4688.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>12.0</td>\n",
              "      <td>Propsh Hontichre</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>8693 rows × 14 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-f4d02ffa-5b38-43a9-800a-76d67618075b')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-f4d02ffa-5b38-43a9-800a-76d67618075b button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-f4d02ffa-5b38-43a9-800a-76d67618075b');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-c2e92b9a-a9b0-46c5-a16b-1ec6700df4a4\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c2e92b9a-a9b0-46c5-a16b-1ec6700df4a4')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-c2e92b9a-a9b0-46c5-a16b-1ec6700df4a4 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 660
        }
      ],
      "source": [
        "my_train"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 661,
      "metadata": {
        "id": "RbYWZmQDBhmU"
      },
      "outputs": [],
      "source": [
        "X_train = my_train.drop(columns=['Name', 'Transported','PassengerId'])\n",
        "X_test = my_test.drop(columns=['Name', 'PassengerId'])\n",
        "\n",
        "y_train = my_train['Transported']\n",
        "\n",
        "train_ids = my_train['PassengerId']\n",
        "test_ids = my_test['PassengerId']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 662,
      "metadata": {
        "id": "iIk1nM5sCDsn"
      },
      "outputs": [],
      "source": [
        "y_train = y_train.map({True:1, False:0})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 663,
      "metadata": {
        "id": "QflEyn65A7n7"
      },
      "outputs": [],
      "source": [
        "from sklearn.impute import SimpleImputer\n",
        "simple = SimpleImputer(strategy='most_frequent')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 664,
      "metadata": {
        "id": "ISzQs0CfA8wH"
      },
      "outputs": [],
      "source": [
        "X_train = pd.DataFrame(simple.fit_transform(X_train), columns = X_train.columns)\n",
        "X_test = pd.DataFrame(simple.transform(X_test), columns = X_test.columns)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 665,
      "metadata": {
        "id": "6mB33OGM1lsd"
      },
      "outputs": [],
      "source": [
        "X_train['> mean age'] = X_train['Age'] >= X_train['Age'].mean()\n",
        "X_test['> mean age'] = X_test['Age'] >= X_test['Age'].mean()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 666,
      "metadata": {
        "id": "kHbxQGaL3hYD"
      },
      "outputs": [],
      "source": [
        "X_train['/2 mean age'] = (X_train['Age']) <= (X_train['Age'].mean()/2)\n",
        "X_test['/2 mean age'] = (X_test['Age']) <= (X_test['Age'].mean()/2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 667,
      "metadata": {
        "id": "hNuZT89W4My6"
      },
      "outputs": [],
      "source": [
        "X_train['toddler'] = X_train['Age'] <=3\n",
        "X_test['toddler'] = X_test['Age'] <= 3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 668,
      "metadata": {
        "id": "pMMhot8u76MR"
      },
      "outputs": [],
      "source": [
        "#X_train[['toddler', 'Transported']].loc[X_train['toddler']==True].sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 669,
      "metadata": {
        "id": "2GgzIu1IEC7n"
      },
      "outputs": [],
      "source": [
        "X_train['deck'] = X_train['Cabin'].str.split('/', expand = True)[0]\n",
        "X_train['num'] = X_train['Cabin'].str.split('/', expand = True)[1]\n",
        "X_train['side'] = X_train['Cabin'].str.split('/', expand = True)[2]\n",
        "\n",
        "X_test['deck'] = X_test['Cabin'].str.split('/', expand = True)[0]\n",
        "X_test['num'] = X_test['Cabin'].str.split('/', expand = True)[1]\n",
        "X_test['side'] = X_test['Cabin'].str.split('/', expand = True)[2]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 670,
      "metadata": {
        "id": "ZBPddzeKBDGj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e88ce842-685f-4723-c33e-7af64c219bb5"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "HomePlanet      0\n",
              "CryoSleep       0\n",
              "Cabin           0\n",
              "Destination     0\n",
              "Age             0\n",
              "VIP             0\n",
              "RoomService     0\n",
              "FoodCourt       0\n",
              "ShoppingMall    0\n",
              "Spa             0\n",
              "VRDeck          0\n",
              "> mean age      0\n",
              "/2 mean age     0\n",
              "toddler         0\n",
              "deck            0\n",
              "num             0\n",
              "side            0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 670
        }
      ],
      "source": [
        "X_train.isna().sum()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4zlG4lM3FBCU"
      },
      "source": [
        "## Encodings"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 671,
      "metadata": {
        "id": "7EUpmrIgExG4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "293a39ec-17a3-4810-8065-9459ba90eef2"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "HomePlanet         3\n",
              "CryoSleep          2\n",
              "Cabin           6560\n",
              "Destination        3\n",
              "Age               80\n",
              "VIP                2\n",
              "RoomService     1273\n",
              "FoodCourt       1507\n",
              "ShoppingMall    1115\n",
              "Spa             1327\n",
              "VRDeck          1306\n",
              "> mean age         2\n",
              "/2 mean age        2\n",
              "toddler            2\n",
              "deck               8\n",
              "num             1817\n",
              "side               2\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 671
        }
      ],
      "source": [
        "X_train.nunique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 672,
      "metadata": {
        "id": "ZxsGZtMeFpdX"
      },
      "outputs": [],
      "source": [
        "!pip install --upgrade category_encoders -q"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 673,
      "metadata": {
        "id": "6fjqU5_LFEJ_"
      },
      "outputs": [],
      "source": [
        "import category_encoders  as ce\n",
        "from sklearn.preprocessing import OneHotEncoder"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 674,
      "metadata": {
        "id": "Rmknm_MDH433"
      },
      "outputs": [],
      "source": [
        "bin_encoded = ce.BinaryEncoder(cols=['HomePlanet','Destination'])\n",
        "\n",
        "X_train = bin_encoded.fit_transform(X_train)\n",
        "X_test = bin_encoded.transform(X_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 675,
      "metadata": {
        "id": "-hiOYbQQE18c"
      },
      "outputs": [],
      "source": [
        "oneHot_encoder = OneHotEncoder()\n",
        "\n",
        "encoded_cryosleep_train = oneHot_encoder.fit_transform(X_train[['CryoSleep']]).todense().astype(int)\n",
        "encoded_cryosleep_test = oneHot_encoder.transform(X_test[['CryoSleep']]).todense().astype(int)\n",
        "\n",
        "encoded_VIP_train = oneHot_encoder.fit_transform(X_train[['VIP']]).todense().astype(int)\n",
        "encoded_VIP_test = oneHot_encoder.transform(X_test[['VIP']]).todense().astype(int)\n",
        "\n",
        "encoded_mean_age_train = oneHot_encoder.fit_transform(X_train[['> mean age']]).todense().astype(int)\n",
        "encoded_mean_age_test = oneHot_encoder.transform(X_test[['> mean age']]).todense().astype(int)\n",
        "\n",
        "encoded_toddler_train = oneHot_encoder.fit_transform(X_train[['toddler']]).todense().astype(int)\n",
        "encoded_toddler_test = oneHot_encoder.transform(X_test[['toddler']]).todense().astype(int)\n",
        "\n",
        "encoded_half_mean_age_train = oneHot_encoder.fit_transform(X_train[['/2 mean age']]).todense().astype(int)\n",
        "encoded_half_mean_age_test = oneHot_encoder.transform(X_test[['/2 mean age']]).todense().astype(int)\n",
        "\n",
        "encoded_side_train = oneHot_encoder.fit_transform(X_train[['side']]).todense().astype(int)\n",
        "encoded_side_test = oneHot_encoder.transform(X_test[['side']]).todense().astype(int)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 676,
      "metadata": {
        "id": "kFZTcXWYGv0J"
      },
      "outputs": [],
      "source": [
        "X_train['CryoSleep'] = encoded_cryosleep_train\n",
        "X_train['VIP'] = encoded_VIP_train\n",
        "X_train['> mean age'] = encoded_mean_age_train\n",
        "X_train['toddler'] = encoded_toddler_train\n",
        "X_train['/2 mean age'] = encoded_half_mean_age_train\n",
        "X_train['side'] = encoded_side_train\n",
        "\n",
        "\n",
        "X_test['CryoSleep'] = encoded_cryosleep_test\n",
        "X_test['VIP'] =encoded_VIP_test\n",
        "X_test['> mean age'] = encoded_mean_age_test\n",
        "X_test['toddler'] = encoded_toddler_test\n",
        "X_test['/2 mean age'] = encoded_half_mean_age_test\n",
        "X_test['side'] = encoded_side_test"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 677,
      "metadata": {
        "id": "GPO3_s8jJt4x"
      },
      "outputs": [],
      "source": [
        "meanEncod = ce.TargetEncoder(cols = ['Cabin','deck'])\n",
        "\n",
        "X_train = meanEncod.fit_transform(X_train, y_train)\n",
        "X_test =  meanEncod.transform(X_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 678,
      "metadata": {
        "id": "dGtw0QWqNbkW"
      },
      "outputs": [],
      "source": [
        "X_train[['Age']] = X_train[['Age']].astype(int)\n",
        "X_train[['RoomService']] = X_train[['RoomService']].astype(float)\n",
        "X_train[['FoodCourt']] = X_train[['FoodCourt']].astype(float)\n",
        "X_train[['ShoppingMall']] = X_train[['ShoppingMall']].astype(float)\n",
        "X_train[['Spa']] = X_train[['Spa']].astype(float)\n",
        "X_train[['VRDeck']] = X_train[['VRDeck']].astype(float)\n",
        "X_train[['num']] = X_train[['num']].astype(float)\n",
        "\n",
        "\n",
        "X_test[['Age']] = X_test[['Age']].astype(int)\n",
        "X_test[['RoomService']] = X_test[['RoomService']].astype(float)\n",
        "X_test[['FoodCourt']] = X_test[['FoodCourt']].astype(float)\n",
        "X_test[['ShoppingMall']] = X_test[['ShoppingMall']].astype(float)\n",
        "X_test[['Spa']] = X_test[['Spa']].astype(float)\n",
        "X_test[['VRDeck']] = X_test[['VRDeck']].astype(float)\n",
        "X_test[['num']] = X_test[['num']].astype(float)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 679,
      "metadata": {
        "id": "EEhSMA6JJIUS",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0808e3ba-31c3-4181-851d-c8f40f2daaf3"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "HomePlanet_0         1.000000\n",
              "HomePlanet_1         1.000000\n",
              "CryoSleep            1.000000\n",
              "Cabin                0.609930\n",
              "Destination_0        1.000000\n",
              "Destination_1        1.000000\n",
              "Age                 79.000000\n",
              "VIP                  1.000000\n",
              "RoomService      14327.000000\n",
              "FoodCourt        29813.000000\n",
              "ShoppingMall     23492.000000\n",
              "Spa              22408.000000\n",
              "VRDeck           24133.000000\n",
              "> mean age           1.000000\n",
              "/2 mean age          1.000000\n",
              "toddler              1.000000\n",
              "deck                 0.734275\n",
              "num               1894.000000\n",
              "side                 1.000000\n",
              "dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 679
        }
      ],
      "source": [
        "X_train.max()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 680,
      "metadata": {
        "id": "sApX4hynKKDG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ab0f2a85-1077-4e3c-cfbf-04c05156ab4d"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "HomePlanet_0     0.000000\n",
              "HomePlanet_1     0.000000\n",
              "CryoSleep        0.000000\n",
              "Cabin            0.403999\n",
              "Destination_0    0.000000\n",
              "Destination_1    0.000000\n",
              "Age              0.000000\n",
              "VIP              0.000000\n",
              "RoomService      0.000000\n",
              "FoodCourt        0.000000\n",
              "ShoppingMall     0.000000\n",
              "Spa              0.000000\n",
              "VRDeck           0.000000\n",
              "> mean age       0.000000\n",
              "/2 mean age      0.000000\n",
              "toddler          0.000000\n",
              "deck             0.357306\n",
              "num              0.000000\n",
              "side             0.000000\n",
              "dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 680
        }
      ],
      "source": [
        "X_train.min()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "R6iUJzIEKQIh"
      },
      "source": [
        "## Train model"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 681,
      "metadata": {
        "id": "QJaoOHsvKTB8"
      },
      "outputs": [],
      "source": [
        "import xgboost as xgb\n",
        "import numpy as np\n",
        "from sklearn.metrics import roc_auc_score, confusion_matrix, accuracy_score\n",
        "from sklearn import tree"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 682,
      "metadata": {
        "id": "-slu8sy4KbM2"
      },
      "outputs": [],
      "source": [
        "from sklearn.model_selection import RandomizedSearchCV"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 683,
      "metadata": {
        "id": "RWR41EoUKde1"
      },
      "outputs": [],
      "source": [
        "classifierXGB = xgb.XGBClassifier(objective = 'binary:logistic')\n",
        "param_dist = {\n",
        "      'n_estimators':np.arange(10, 120, 20),\n",
        "      'learning_rate' : [0.05,0.10,0.15,0.20,0.25,0.30],\n",
        "      'max_depth' : np.arange(2, 150, 5),\n",
        "      'min_child_weight' : [ 1, 3, 5, 7 ],\n",
        "      'gamma': [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],\n",
        "      'colsample_bytree' : [ 0.3, 0.4, 0.5 , 0.7 ]\n",
        "}\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 684,
      "metadata": {
        "id": "ZgpD2kcCKjBs"
      },
      "outputs": [],
      "source": [
        "rs_xg_class = RandomizedSearchCV(classifierXGB, param_distributions = param_dist, n_iter=13, random_state = 13, scoring='accuracy')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 685,
      "metadata": {
        "id": "zZUwddnnKoXf"
      },
      "outputs": [],
      "source": [
        "rs_xg_class.fit(X_train, y_train)\n",
        "preds = rs_xg_class.predict(X_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 686,
      "metadata": {
        "id": "7P_sPLfjNx5O"
      },
      "outputs": [],
      "source": [
        "preds_train = rs_xg_class.predict(X_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 687,
      "metadata": {
        "id": "n1dLuX7iKp92",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "995db65a-ceec-4891-dd2f-bebd42f99ca3"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'n_estimators': 70,\n",
              " 'min_child_weight': 1,\n",
              " 'max_depth': 112,\n",
              " 'learning_rate': 0.3,\n",
              " 'gamma': 0.3,\n",
              " 'colsample_bytree': 0.7}"
            ]
          },
          "metadata": {},
          "execution_count": 687
        }
      ],
      "source": [
        "rs_xg_class.best_params_"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 688,
      "metadata": {
        "id": "g0HVN_V-Krod"
      },
      "outputs": [],
      "source": [
        "model = rs_xg_class.best_estimator_"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 689,
      "metadata": {
        "id": "GjcjW369KtJE",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 248
        },
        "outputId": "2ce874ce-4103-4d44-b643-fd426c958fc0"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "XGBClassifier(base_score=None, booster=None, callbacks=None,\n",
              "              colsample_bylevel=None, colsample_bynode=None,\n",
              "              colsample_bytree=0.7, device=None, early_stopping_rounds=None,\n",
              "              enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "              gamma=0.3, grow_policy=None, importance_type=None,\n",
              "              interaction_constraints=None, learning_rate=0.3, max_bin=None,\n",
              "              max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "              max_delta_step=None, max_depth=112, max_leaves=None,\n",
              "              min_child_weight=1, missing=nan, monotone_constraints=None,\n",
              "              multi_strategy=None, n_estimators=70, n_jobs=None,\n",
              "              num_parallel_tree=None, random_state=None, ...)"
            ],
            "text/html": [
              "<style>#sk-container-id-33 {color: black;background-color: white;}#sk-container-id-33 pre{padding: 0;}#sk-container-id-33 div.sk-toggleable {background-color: white;}#sk-container-id-33 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-33 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-33 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-33 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-33 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-33 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-33 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-33 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-33 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-33 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-33 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-33 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-33 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-33 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-33 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-33 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-33 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-33 div.sk-item {position: relative;z-index: 1;}#sk-container-id-33 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-33 div.sk-item::before, #sk-container-id-33 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-33 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-33 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-33 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-33 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-33 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-33 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-33 div.sk-label-container {text-align: center;}#sk-container-id-33 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-33 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-33\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>XGBClassifier(base_score=None, booster=None, callbacks=None,\n",
              "              colsample_bylevel=None, colsample_bynode=None,\n",
              "              colsample_bytree=0.7, device=None, early_stopping_rounds=None,\n",
              "              enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "              gamma=0.3, grow_policy=None, importance_type=None,\n",
              "              interaction_constraints=None, learning_rate=0.3, max_bin=None,\n",
              "              max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "              max_delta_step=None, max_depth=112, max_leaves=None,\n",
              "              min_child_weight=1, missing=nan, monotone_constraints=None,\n",
              "              multi_strategy=None, n_estimators=70, n_jobs=None,\n",
              "              num_parallel_tree=None, random_state=None, ...)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-33\" type=\"checkbox\" checked><label for=\"sk-estimator-id-33\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">XGBClassifier</label><div class=\"sk-toggleable__content\"><pre>XGBClassifier(base_score=None, booster=None, callbacks=None,\n",
              "              colsample_bylevel=None, colsample_bynode=None,\n",
              "              colsample_bytree=0.7, device=None, early_stopping_rounds=None,\n",
              "              enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "              gamma=0.3, grow_policy=None, importance_type=None,\n",
              "              interaction_constraints=None, learning_rate=0.3, max_bin=None,\n",
              "              max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "              max_delta_step=None, max_depth=112, max_leaves=None,\n",
              "              min_child_weight=1, missing=nan, monotone_constraints=None,\n",
              "              multi_strategy=None, n_estimators=70, n_jobs=None,\n",
              "              num_parallel_tree=None, random_state=None, ...)</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 689
        }
      ],
      "source": [
        "model.fit(X_train, y_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 690,
      "metadata": {
        "id": "lRz9T-W_PCKu",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b1f5d5ab-5834-4e38-c408-a506d5bb396d"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.9941332106292419"
            ]
          },
          "metadata": {},
          "execution_count": 690
        }
      ],
      "source": [
        "accuracy_score(y_train, preds_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 692,
      "metadata": {
        "id": "RgQ7jz5HPMJA"
      },
      "outputs": [],
      "source": [
        "cm = confusion_matrix(y_train, preds_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 693,
      "metadata": {
        "id": "8QROy3kJI2EM"
      },
      "outputs": [],
      "source": [
        "percentage_right_not_transp = (cm[0][0]*100 / (cm[0][0] + cm[0][1]))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 694,
      "metadata": {
        "id": "dY4yIRopJBk1"
      },
      "outputs": [],
      "source": [
        "percentage_right_transp  = (cm[1][1]*100 / (cm[1][1] + cm[1][0]))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 695,
      "metadata": {
        "id": "66otGEhsJZuK",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "outputId": "6ee62e14-876d-49c3-ffab-469ae9be9752"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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U2hoqHx8fFSvXj3t3r1bhQsXtroaJr8eqZWV1tjnZcuWWefdHDlyKDIyUrt27bLLExsbqy5duih//vzy9PRUvnz51KJFC7uytmzZooiICAUGBsrb21tFihTRs88+e9tjstlsmjFjhi5evJjifJnRtm3FihWqVq2avL297X4xuhuFCxdWx44dNX369Duea6UbvZoaN24sf39/+fn5qX79+nbde2fOnKknnnhCklSvXj3rWO+la/vtjnvGjBl67LHHFBQUJE9PT5UtW1ZTp05Ns4zbXRdI/+tGXKJECXl5eSlPnjx65JFHFB0dbeXp3Lmz/Pz8dPDgQUVERMjX11ehoaEaMWKEblxz/c/FixfVr18/FShQQJ6enipVqpTefffdFPlsNpt69OihOXPmqFy5cvL09NS0adOsnhDDhw9Ptfvsnj179Pjjjyt37tzy8vJStWrV9N1336U4/l27dumxxx6Tt7e38ufPr5EjRyopKSljb0Qavv32W0VGRlrdyYsVK6a33npL169ft8uXfF2we/du1atXTz4+PnrggQc0ZsyYFGUePXpULVu2lK+vr4KCgtSnT58U34e0pLdduNv2KzV3aqfj4+OVK1cueXp6Wmlubm7WOeTmfJIUHBxs9/zka+Rb86anzIzUMzVBQUHy8fFJ8xrlZne6nklv25/s+PHj+uGHH9S6dWurF6d0o02Oi4vT22+/LRcXF128eDHVz/O9vseZ2fbfrszMbvuTu3sfOnRIS5cuTTHE6sSJE+ratauCg4Pl5eWlBx98MEWv2ttdO2SF5PZ89+7deuqpp5QrVy498sgjkqTff/9dnTt3toaQh4SE6Nlnn9Xp06dTLSM99013un9Lfg3nzZun119/XSEhIfL19VXz5s31999/p6j/ggULVLVqVXl7eyswMFBPP/203dAP6X9tx4EDB9SkSRPlyJFDHTp0UN26dbV06VIdPnzYeq9uvt5KSEjQ0KFDVbx4cXl6eqpAgQIaMGBAinNiQkKC+vTpo7x58ypHjhxq3rx5ih4y6dWwYUNdvHjRru1LjwwFAhYvXqyiRYvq4YcfTlf+5557Tm+++aaqVKmi8ePHq06dOoqKikrxBZek/fv36/HHH1fDhg01btw45cqVS507d7Yu+lq3bm11PXzyySc1e/bsDI/N2LVrl5o2baqEhASNGDFC48aNU/Pmze84Yd2qVasUERGhEydOaNiwYerbt682btyoWrVqpToOsm3btjp//ryioqLUtm1bzZw5M9Vu3Glp3bq1bDabvvnmGytt7ty5Kl26tKpUqZIi/8GDB7Vo0SI1bdpU7733nvr3768dO3aoTp061oVimTJlNGLECEk3uqbPnj1bs2fPVu3ata1yTp8+rcaNG6tSpUqaMGGC6tWrl2r9Jk6cqLx586pTp07WhcOHH36olStX6v33379td9Vr165p8+bNKY4j+cuRWmPo7e2t3377zWo0EhISUs3n4+Mj6cZYw4wyxiguLk6BgYGpbj99+rROnDihLVu2qEuXLpKk+vXrp8g3c+ZM+fr6ytvbW2XLltXcuXPTtf/Y2FhJSnP/6c3bpUsX+fv7y8vLS/Xq1dOWLVvstqf1Ot/utbtTmcn+/PNP64YtJCREQ4YM0bVr11LsP6337urVq9a4xt27d+vYsWOqWLGiXnjhBfn6+srX11cVK1bUDz/8kOr+k127dk3z58/Xww8/nOqNcHrqmd5jr169upYvX66VK1dq3759GjdunB566CHrGKZNm3bXY8hmzJih999/Xy+88ILGjRun3Llzp5pv6dKlateundzd3RUVFaXWrVura9euaX4P5s6dq7Fjx+rFF1/UyJEj9ddff6l169bWa/Diiy+qYcOGkmSdJ1Lr/nmzQYMGafjw4apWrZrGjh2rEiVKKCIiQhcvXryrY0/ed2RkpPz8/PTOO+9oyJAh2r17tx555BG7826bNm20cOFCdenSRVOmTFGvXr10/vx5a3zuiRMnFB4err/++kuvvfaa3n//fXXo0CHFXA+p7f/RRx+Vp6dnivNlRtq2vXv36sknn1TDhg01ceLETJlw8I033lBiYmKq45pvtmvXLj366KPavn27BgwYoCFDhujQoUOqW7eufvnlF0lS7dq11atXL0nS66+/bh3rzd0/70Zaxz116lQVKlRIr7/+usaNG6cCBQro5ZdftoJPN7vTdYF040Jy+PDhqlevniZPnqw33nhDBQsW1K+//mpX1vXr19WoUSMFBwdrzJgxqlq1qoYOHWrXBdcYo+bNm2v8+PFq1KiR3nvvPZUqVUr9+/dX3759U9RvzZo16tOnj9q1a6eJEyeqevXqVlCjVatW1muZfDOwa9cu1axZU3/88Ydee+01jRs3Tr6+vmrZsqUWLlxolRsbG6t69epp27Zteu2119S7d2999tlnmjhx4t2/ITeZOXOm/Pz81LdvX02cOFFVq1bVm2++qddeey1F3n///VeNGjXSgw8+qHHjxql06dIaOHCgli1bZuW5fPmy6tevrxUrVqhHjx5644039OOPP2rAgAHpqk9624W7ab/SOv47tdN169bVrl27NGTIEO3fv18HDhzQW2+9pS1bttgdV7Vq1eTr66shQ4ZozZo1+ueff7Ru3ToNGDBA1atXt+tmnt4yM1LPZGfPntXJkye1Y8cOPffcc4qPj0/1GiUxMVGnTp3SsWPHtHLlSg0ePFg5cuSw2q2bpbftv9mXX36ppKQkdejQwS591apV8vf31z///KNSpUpZP1q99NJLdoGOe3mPM7Ptv1OZmd32lylTRrNnz1ZgYKAqVapknTvy5s2ry5cvq27dupo9e7Y6dOigsWPHKiAgQJ07d071nJDea4fM8sQTT+jSpUsaNWqUNS9EdHS0Dh48qC5duuj9999X+/bt9eWXX6pJkyYpgqrSne+bMnL/9vbbb2vp0qUaOHCgevXqpejoaDVo0MBu7rWZM2eqbdu2cnV1VVRUlJ5//nl98803euSRR1IExRITExUREaGgoCC9++67atOmjd544w1VqlRJgYGB1nuV/H4nJSWpefPmevfdd9WsWTO9//77atmypcaPH6927drZlf3cc89pwoQJCg8P1+jRo+Xu7q7IyMi7eh/Kli0rb2/vjE/Cnt6uA+fOnTOSTIsWLdKVf9u2bUaSee655+zSX331VSPJrFmzxkorVKiQkWTWr19vpZ04ccJ4enqafv36WWlpdW3t1KlTqt0zhg4date9dfz48UaSOXnyZJr1Tt7Hzd3nK1WqZIKCgszp06ettO3btxsXFxfTsWPHFPt79tln7cps1aqVyZMnT5r7vPk4kruhPv7446Z+/frGmBtdDkNCQszw4cNTfQ2uXLmSoqvVoUOHjKenpxkxYoSVdruhAXXq1DGSzLRp01Lddmt3wxUrVhhJZuTIkdaQkdSGM9xq//79RpJ5//337dJPnjxpbDab6dq1q136nj17jCQjyeo22LNnT+Pi4pKi23z79u2NJNOjR4871uNWs2fPNpLMJ598kup2T09Pqx558uSxG6qQ7OGHHzYTJkww3377rZk6daopX768kWSmTJlyx/137drVuLq6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SkpKSnXcZGZJ67g3bNigBg0aWPPt5M2b1xrneWt7lZ7rghEjRujs2bMqWbKkKlSooP79++v3339P8TwXFxcVLVrULq1kyZKSZA01OXz4sEJDQ61Z3pMlD5O4l/d2//79MsZoyJAhKT7TycMTkj/Xhw8fVokSJVKUkdp7eTd27dqlVq1aKSAgQP7+/sqbN6+efvppSSnfg/z586eY1+PW9+Dw4cMqXrx4inzprW9624V7bb9Sk1Y73aNHDy1evFhffvml2rdvrw4dOmjVqlXKly+f3VxYBw8eVL169fTss8/q9ddfV4sWLTR06FBNmTJFX331ld0QivSWmZF6JgsLC1NERIReeuklrVixQp9//rkGDRqUIp+/v78aNGigFi1a6J133lG/fv3UokWLOy47lp62f86cOZKUYliA9L82/cknn7RLT24PY2JiJN39e5wVbX96ysyKtv9WyeeDW1d1yIzzUmZIbX9nzpzRK6+8ouDgYHl7eytv3rxWvtTuS+50XZKR+7dbz502m03Fixe3O89LqZ+fSpcuneL1dHNzs1apSo99+/Zp165dKc7zye3Nzed5FxcXFStWzO7593KeN8bccU6nW2UoEBAaGprq2qS3k94KpXUDltoNY3r3cevJytvbW+vXr9eqVav0zDPP6Pfff1e7du3UsGHDO97UZMS9HEsyT09PtW7dWrNmzdLChQtvewIZNWqU+vbtq9q1a+vzzz/XihUrFB0drXLlymVocqG0JqtJy2+//WZ9oHfs2JGu5ySfTFO76QgICNC3336rw4cPa926dfrrr780e/ZsHT9+XHnz5lXOnDmtvI8//riOHTumTZs2KSYmRocPH7Yu8pK/bHdy7tw5NW7cWGfPntXy5cvTvRRXsWLFVLlyZavRu53km9gzZ86k2LZ9+3Y1b95c5cuX11dffSU3t7RX8xw+fLimTJmi0aNHZ2hd2QIFCujq1at2wapy5cpp586d2rlzp3788UcdO3ZMzz//vE6dOpWu1y61MtPKJ6U89rfffltxcXH68ccf9fvvv2vz5s3W5zR5/8nvxa0TMEk3JkJK66Z10aJFunTpUqoXIhmtZ1p573Ts48ePl5ubm3r06KG///5bP/30kzUmecyYMVq3bl26JoPJ6PcxvTLj/HS30nuuTv48zJ49W9HR0Ske3377rZW3d+/e+vPPPxUVFSUv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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.heatmap(cm, annot=True, cmap='Greens',fmt=\".1f\")\n",
        "plt.title('Confusion Matrix ({}% right guess for \"Not Transported\" and {}% for \"Transported\")'.format(percentage_right_not_transp , percentage_right_transp))\n",
        "plt.xlabel('Predicted')\n",
        "plt.ylabel('Actual')\n",
        "plt.show()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 696,
      "metadata": {
        "id": "UYOccUTVPUI-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "dfb129da-f2bc-4608-e990-b5d4243dc9f1"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       0013_01\n",
              "1       0018_01\n",
              "2       0019_01\n",
              "3       0021_01\n",
              "4       0023_01\n",
              "         ...   \n",
              "4272    9266_02\n",
              "4273    9269_01\n",
              "4274    9271_01\n",
              "4275    9273_01\n",
              "4276    9277_01\n",
              "Name: PassengerId, Length: 4277, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 696
        }
      ],
      "source": [
        "test_ids"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 697,
      "metadata": {
        "id": "EtU82mnyP2so"
      },
      "outputs": [],
      "source": [
        "\n",
        "compare_df = pd.DataFrame(test_ids)\n",
        "\n",
        "\n",
        "#y_predict_test = model.predict(X_test)\n",
        "\n",
        "\n",
        "compare_df['Transported'] = preds\n",
        "compare_df['Transported'] = compare_df['Transported'].map({1:True, 0:False})\n",
        "\n",
        "from pathlib import Path\n",
        "filepath = Path('/content/drive/MyDrive/Organizacion De Datos/trabajo_practico_2/predicciones_XGBoost.csv')\n",
        "compare_df.to_csv(filepath,index=False)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMmAvxYm9mcPUXIht7ojddO",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}