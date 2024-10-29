def jump(self, nums):
        #Initialize minJumps to 0 that will count 
        # min number of jumps to reach the end
        minJumps = 0
        # left and right pointer initialized to zero 
        # this will keep track of our positioning
        # left will keep track of current nums[i]
        # right will keep track of position we jump to 
        l = r = 0
         # while loop that continues until r reaches the end of the list
        while r < len(nums) - 1:
            # initialize a variable called farthest to 0
            # will keep track of the farthest position we can go based off of the jump
            farthest = 0
            # for loop to check the values between left and right
            for i in range(l,r + 1):
                # make farthest equal to the max jump from position at i
                # i + nums[i] gives us how many times we have to jump from position at i
                farthest = max(farthest, i + nums[i])
            # then we make the left pointer equal the right pointer + 1 
            # so that we can check the next section
            l = r + 1
            # we make r = the farthest which will take us to the position we can jump 
            # the farthest to this way we dont have to keep checking each position
            r = farthest
            # since we made a jump we increment minJumps by 1
            minJumps += 1
        # if we reach the end of the list we will return minJumps
        return minJumps