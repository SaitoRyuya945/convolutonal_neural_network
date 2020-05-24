# 畳み込み層作成プロジェクト

## 1回目畳みこみ層の仕組みを理解しよう

　畳み込み層では、「畳み込み演算」という処理を行う必要がある。  
これは、画像処理でのフィルター演算と同じ処理を行うことで、  
判別に必要な情報を抽出する仕組みである。
これを用いることで画像内のコーナーや、領域が変化している部分を識別できる。
このようにフィルターによって、画像の中の自分が欲しい情報だけを持ってくることが出来き、  
それにより、様々な用途に使うことができる。(例：画像の中の人だけを切り抜くなど)

計算方法を下記に記載する。
画像とフィルターを行列とみなして、フィルターの大きさにあわせ上から、  
行列の要素同士を掛け合わせる。

計算例  
$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\\\
0 & 1 & 2 & 3 \\\\
3 & 0 & 1 & 2 \\\\
2 & 3 & 0 & 1
\end{bmatrix}
$$  

この行列を下記のように3×3のフィルタを用いて計算してく。

左上とフィルターの計算  
$$
\begin{bmatrix}
1 & 2 & 3 &  \\\\
0 & 1 & 2 &  \\\\
3 & 0 & 1 &  \\\\
  &   &   &  
\end{bmatrix}  
\ast  
\begin{bmatrix}
0 & 1 & 2  \\\\
2 & 1 & 1  \\\\
1 & 0 & 2
\end{bmatrix}
= \begin{bmatrix}
16 &  \\\\
 &  \\\\
\end{bmatrix}
$$  

右上とフィルターの計算  
$$
\begin{bmatrix}
  & 2 & 3 & 4 \\\\
  & 1 & 2 & 3 \\\\
  & 0 & 1 & 2 \\\\
  &   &   &
\end{bmatrix}  
\ast  
\begin{bmatrix}
0 & 1 & 2  \\\\
2 & 1 & 1  \\\\
1 & 0 & 2
\end{bmatrix}
= \begin{bmatrix}
16 & 22 \\\\
 &  \\\\
\end{bmatrix}
$$  

左下とフィルターの計算  
$$
\begin{bmatrix}
  &   &   &   \\\\
0 & 1 & 2 &   \\\\
3 & 0 & 1 &   \\\\
2 & 3 & 0 &
\end{bmatrix}  
\ast  
\begin{bmatrix}
0 & 1 & 2  \\\\
2 & 1 & 1  \\\\
1 & 0 & 2
\end{bmatrix}
= \begin{bmatrix}
16 & 22 \\\\
14 &  \\\\
\end{bmatrix}
$$  

右下とフィルターの計算  
$$
\begin{bmatrix}
  &   &   &   \\\\
  & 1 & 2 & 3 \\\\
  & 0 & 1 & 2 \\\\
  & 3 & 0 & 1
\end{bmatrix}  
\ast  
\begin{bmatrix}
0 & 1 & 2  \\\\
2 & 1 & 1  \\\\
1 & 0 & 2
\end{bmatrix}
= \begin{bmatrix}
16 & 22 \\\\
14 & 16 \\\\
\end{bmatrix}
$$  

この計算方法をもとに畳み込み演算のアルゴリズムを作成していく。  
ここで、パティングとストライドについて触れていく。  

### パティング

上記のフィルター計算を見てもらうと、入力した画像サイズより、  
出力した画像サイズの方が小さくなっている。畳み込み演算では、何回も  
このフィルター計算を行うことになるので、どこかで出力サイズが１になる可能性もある。  
このような状況を回避するため、入力画像の周囲に固定のデータ（0など）で埋め処理を行う。  
これをパティングと呼ぶ。

### ストライド

フィルターを適用する間隔のことをストライドと呼ぶ。ストライドを大きくすると、  
出力した画像サイズの方が小さくなっている。畳み込み演算では、何回も

### 出力画像サイズの計算方法

上記のフィルター計算、パティング、ストライドを用いて出力画像サイズを下記の式で計算できる。  
入力画像サイズ(IH,IW)、フィルター(FH,FW)、パティング(P)、ストライド(S)、  
出力画像サイズ(OH,OW)とすると、

$$
OH = \frac{IH+2P-FH}{S} + 1  
$$

$$
OW = \frac{IW+2P-FW}{S} + 1
$$

先ほどのフィルター計算を例に計算してみると  
$$
OH = \frac{4+0-3}{1} + 1 = 2
$$

$$
OW = \frac{4+0-3}{1} + 1 = 2
$$

となり、計算結果が合致している。

### アルゴリズム

今回は、パティング0、ストライド1で固定する。（簡略化のため）
出力サイズが割り切れなければ、エラーを出力する

1. 入力画像サイズ(4,4)と、フィルターサイズ(3,3)を取得する。
2. 出力サイズを計算し、サイズ分の空行列を作成する。
3. 入力画像の(0,0)から(2,2)を、フィルターで掛け合わせ計算する。
4. ストライド分、横に移動する。この時、出力横サイズ分移動したら、縦に移動する。
5. 出力サイズ分計算し終えたら終了。

### 発展形：部分行列を用いた畳み込み演算の行列計算

上記の処理を簡略化するために、下記のように、部分行列に変換する。
((i、j)行列から(i、j、k、l)行列に変換する)  
このプロジェクトのソースコードはこちらのアルゴリズムを使用している。

$$
\begin{bmatrix}
1&2&3&4 \\\\
0&1&2&3 \\\\
3&0&1&2 \\\\
2&3&0&1 \\\\
\end{bmatrix}
= \begin{bmatrix}
\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}&\begin{bmatrix}
2&3 \\\\
1&2 \\\\
\end{bmatrix}&\begin{bmatrix}
3&4 \\\\
2&3 \\\\
\end{bmatrix} \\\\
\begin{bmatrix}
0&1 \\\\
3&0 \\\\
\end{bmatrix}&\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}&\begin{bmatrix}
2&3 \\\\
1&2 \\\\
\end{bmatrix} \\\\
\begin{bmatrix}
3&0 \\\\
2&3 \\\\
\end{bmatrix}&\begin{bmatrix}
0&1 \\\\
3&0 \\\\
\end{bmatrix}&\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}
\end{bmatrix}
$$  

次に、部分行列とフィルターを計算していく
$$
\begin{bmatrix}
0&1&2 \\\\
2&1&1 \\\\
1&0&2 \\\\
\end{bmatrix} \ast \begin{bmatrix}
\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}&\begin{bmatrix}
2&3 \\\\
1&2 \\\\
\end{bmatrix}&\begin{bmatrix}
3&4 \\\\
2&3 \\\\
\end{bmatrix} \\\\
\begin{bmatrix}
0&1 \\\\
3&0 \\\\
\end{bmatrix}&\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}&\begin{bmatrix}
2&3 \\\\
1&2 \\\\
\end{bmatrix} \\\\
\begin{bmatrix}
3&0 \\\\
2&3 \\\\
\end{bmatrix}&\begin{bmatrix}
0&1 \\\\
3&0 \\\\
\end{bmatrix}&\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}
\end{bmatrix} = \begin{bmatrix}
0\ast\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}&1\ast\begin{bmatrix}
2&3 \\\\
1&2 \\\\
\end{bmatrix}&2\ast\begin{bmatrix}
3&4 \\\\
2&3 \\\\
\end{bmatrix} \\\\
2\ast\begin{bmatrix}
0&1 \\\\
3&0 \\\\
\end{bmatrix}&1\ast\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}&1\ast\begin{bmatrix}
2&3 \\\\
1&2 \\\\
\end{bmatrix} \\\\
1\ast\begin{bmatrix}
3&0 \\\\
2&3 \\\\
\end{bmatrix}&0\ast\begin{bmatrix}
0&1 \\\\
3&0 \\\\
\end{bmatrix}&2\ast\begin{bmatrix}
1&2 \\\\
0&1 \\\\
\end{bmatrix}
\end{bmatrix}
$$

この(i,j,k,l)のインデックスを持つ行列の(i,j)の要素を総和することにより、  
上記のアルゴリズムの計算と、同等の値を得ることが出来る。
