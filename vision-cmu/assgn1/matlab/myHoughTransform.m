function [H, rhoScale, thetaScale] = myHoughTransform(Im, threshold, rhoRes, thetaRes)
%Your implementation here
[sizeX, sizeY] = size(Im);
thetaScale = linspace(0,180,thetaRes);
M = sqrt(sizeX^2 + sizeY^2);
rhoScale = linspace(0,M,rhoRes);
H = zeros(thetaRes,rhoRes);
for i=1:sizeX
    for j=1:sizeY
        if Im(i,j)>threshold
            for k=1:length(thetaScale)
                rhoTemp = i*cosd(thetaScale(k)) + j*sind(thetaScale(k));
                if rhoTemp >=0 
                    diff = rhoScale(2)-rhoScale(1);
                    rho = floor(rhoTemp/diff) + 1;
                    H(k,rho)= H(k,rho) + 1;
                end
            end
        end
    end
end
end
        
        