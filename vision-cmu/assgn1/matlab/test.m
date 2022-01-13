clc
clear
img = imread('../data/img02.jpg');
% imshow(img)
% RGB = imread('gantrycrane.png');
% I  = imbinarize(img);
% BW = edge(I,'canny');
% [H,T,R] = hough(BW,'RhoResolution',5,'Theta',-90:1:89);
% filter = [-1 5 -6;4 7 0;1 3 2]
% img = [1 1 1;1 1 1;1 1 1];
% f2 = uint8(filter)
% class(filter)
% output = myImageFilter(img,filter);
% imshow(uint8(output))
% x = conv2(img,filter,'same');
[x,y] = myEdgeFilter(img,0.1);
% subplot(1,2,1), imshow(uint8(x))
% subplot(1,2,2), imshow(uint8(y))
[H, rhoScale, thetaScale] = myHoughTransform(x, 220, 200, 200);
[rhos,thetas] = myHoughLines(H, 40);
 imshow(uint8(H))
