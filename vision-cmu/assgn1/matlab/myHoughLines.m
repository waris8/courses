function [rhos, thetas] = myHoughLines(H, nLines)
    %Your implemention here
    [X,Y] = size(H);
    paddedH = padarray(H,[1,2],'both');
    rhos = zeros(nLines,1);
    thetas = zeros(nLines,1);
    count = 0;
    for i=2:X+1
        for j=2:Y+1
            if paddedH(i,j)~=0
                neighbors = [-1 -1 -1 0 0 1 1 1;-1 0 1 -1 1 -1 0 1];
                for k=1:length(neighbors)
                    if paddedH(i-neighbors(1,k),j-neighbors(2,k))>paddedH(i,j)
                        paddedH(i,j)=0;
                    end
                end
                if paddedH(i,j)~=0 && count ~= nLines
                    rhos(count+1) = j;
                    thetas(count+1) = i;
                    count = count+1;
                end
            end
        end
    end
end
        