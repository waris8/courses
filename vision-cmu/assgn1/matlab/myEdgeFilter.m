function [img1, img] = myEdgeFilter(img0, sigma)
    %Your implemention
    [sizeX, sizeY] = size(img0);
    hsize = 2*ceil(3*sigma)+1;
    gaussian = fspecial('gaussian',hsize, sigma);
    imgSmooth = myImageFilter(img0, gaussian);
    sobelY = fspecial('sobel');
    sobelX = sobelY';
    imgX = myImageFilter(imgSmooth,sobelX);
    imgY = myImageFilter(imgSmooth, sobelY);
    img = sqrt(imgX.^2 + imgY.^2);
    paddedImg = padarray(img,[1,1],'both');
    gradientMatrix = rad2deg(atan2(imgX, imgY));
    gradientQuantization = [0 45 90 135 180];
    for i=2:sizeX+1
        for j=2:sizeY+1
            netGradient = paddedImg(i,j);
            tangent = gradientMatrix(i-1,j-1);
            if tangent < 0
                tangent = tangent + 180;
                gradientApprox = gradientQuantization(floor(tangent/45)+1);
                neighborIndexes = zeros(2,2);
                if gradientApprox == 0 || gradientApprox == 180 
                    neighborIndexes = [i j-1;i j+1];
                end
                if gradientApprox == 45 
                    neighborIndexes = [i-1 j+1;i+1 j-1];
                end
                if gradientApprox == 90 
                    neighborIndexes = [i-1 j;i+1 j];
                end
                if gradientApprox == 135 
                    neighborIndexes = [i-1 j-1;i+1 j+1];
                end
                firstNeighborgradient = paddedImg(neighborIndexes(1,1),neighborIndexes(1,2));
                secondNeighborGradient = paddedImg(neighborIndexes(2,1),neighborIndexes(2,2));
                if  netGradient < firstNeighborgradient || netGradient < secondNeighborGradient
                    paddedImg(i,j) = 0;
                end
            end
        end
    end
    img1 = paddedImg(2:sizeX+1, 2:sizeY+1);
end
    
                
        
        
