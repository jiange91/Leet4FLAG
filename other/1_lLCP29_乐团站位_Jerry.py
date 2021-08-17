class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        # layer = int(pow(pow(xPos - (num-1)/2,2) + pow(yPos - (num-1)/2,2), 1/2))
        layer = min(min(yPos,xPos),min( num - xPos - 1, num - yPos - 1))+1;
        n = num
        area = num * num
        center = pow((num-2*(layer-1)),2)
        index = 1 + (area - center) % 9
        # print(layer)
        #右边界
        right = num-layer;
        #左边届
        left = layer-1
        if xPos==left:
            # 在 --- 上
            index += yPos-left 
        elif yPos == right:
            #在   |上
            index += right-left
            index += xPos-left
        elif xPos==right:
            #在 __ 上
            index+=2*(right-left);
            index+=right-yPos;
        else:
            #在 |  上
            index+=3*(right-left);
            index+=right-xPos;
        return index % 9 if index % 9 != 0 else 9;