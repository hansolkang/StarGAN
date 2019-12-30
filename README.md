# StarGAN
얼굴 정확도 향상 테스트를 위한 RaFD Data Augmentation.
데이터는 직접 모은 데이터 + CK + RaFD를 사용하였다.
그런데 생각보다 원하는 만큼의 좋은 결과가 나오지 않았다.

![image](https://user-images.githubusercontent.com/14813279/71571971-69ab4000-2b20-11ea-980a-3ff6a35b486c.png)
![image](https://user-images.githubusercontent.com/14813279/71571978-7039b780-2b20-11ea-8a64-63bcb89514ec.png)
![image](https://user-images.githubusercontent.com/14813279/71571983-75970200-2b20-11ea-9ff4-365229a3ab44.png)
![image](https://user-images.githubusercontent.com/14813279/71571991-7c257980-2b20-11ea-966a-8eb363b4faa5.png)
![image](https://user-images.githubusercontent.com/14813279/71572005-847db480-2b20-11ea-9868-5d83aeb3d1f1.png)

아래의 그림처럼 results 안에 그림은 무표정이고, 무표정으로 GAN을 한 것이 실제로 보기에도 비슷해 보인다. 그래서 아래와 같이 0~7까지 표정(화남, 슬픔, 행복 등등...)으로 나누었고 이를 이용해 표정 분류를 더 잘 할 수 있을 것인가에 대한 실험을 진행해 보았다.
![image](https://user-images.githubusercontent.com/14813279/71572438-7a5cb580-2b22-11ea-87bb-0aedfa4e7683.png)
![image](https://user-images.githubusercontent.com/14813279/71572445-85afe100-2b22-11ea-98aa-2ca9417cb41b.png)

실험은 GAN을 통해서 얻은 데이터를 통해 훈련을 하는 것이다. GAN을 통해서 만들어진 더 많은 데이터를 활용하면 아무래도 데이터가 많다보니 더 강력한 Classifier가 되지 않을까라는 생각에서 출발하였다. 그러나 파일을 입력으로 주거나, CAM을 입력으로 주었을 때 모두 다 별로 좋지 않은 결과가 나타났다.

**StarGAN을 통해서 얻은 결과는 실험에 대하여 크게 영향을 주지 않았다.**
