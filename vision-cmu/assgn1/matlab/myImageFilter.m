function [img1] = myImageFilter(img, h)
    img0 = double(img);
    kernelSize = size(h);
    padSize = floor(size(h)/2);
    paddedImg = padarray(img0,[padSize(1),padSize(2)],'both');
    imageSize = size(img0);
    img1 = zeros(imageSize(1),imageSize(2));
    for i= 1:imageSize(1)
        for j= 1:imageSize(2)
            x = paddedImg(i:i+kernelSize(1)-1,j:j+kernelSize(2)-1);
            img1(i,j) = sum(sum(x.*h));
        end
    end
end

