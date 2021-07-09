class CompetitorInstance:
    def __init__(self):

        self.index = None
        self.true_value = None

        pass

    def onGameStart(self, engine, gameParameters):

        # engine: an instance of the game engine with functions as outlined in the documentation.
        self.engine = engine

        # gameParameters: A dictionary containing a variety of game parameters
        self.gameParameters = gameParameters

    def onAuctionStart(self, index, trueValue):

        # Note that the index of each bots doesn't change in between games.
        self.index = index

        # trueValue is -1 if this bot doesn't know the true value
        if trueValue != -1:
            self.true_value = trueValue

        pass

    def onBidMade(self, whoMadeBid, howMuch):
        # whoMadeBid is the index of the player that made the bid
        # howMuch is the amount that the bid was

        # Here we want to keep track of who made what bids and when so we can
        # learn which bots are which. We need to think of what kind of data
        # structure we want to use for this, which mostly relates to how we want
        # to use the information we get.

        # I think there's two ways we do this - either probabilistically or
        # deterministically. We either come up with some way to encode which
        # bots are our own based off their bids through the way that they bid,
        # or we build a profile of each competitor bot and assign it
        # probabilistically.

        # Obviously, the more obvious our own bidding strategy is, the more
        # obvious it is for other bots to figure out who we are as well. Again,
        # it's not about how many points we score, but how we perform in
        # relation to other bots in our game. For example, you would think that
        # no bot that knows the true value is going to bid above the true value,
        # but maybe this is exactly what we do in order to fool other bots into
        # thinking that we don't know the true value (considering you get 100
        # points for guessing another bot that knows the true value). This is
        # probably a little too advanced at the moment.

        # We also probably want to track when each ID bid last (so if we know
        # that they drop out, we can learn things about them and the true
        # value).

        # NPCs
        # NPCs should be easy to recognise. We have two pieces of information:
        # they have a probability of when they bid, which gets lowers the closer
        # we get to the mean value, and that they only bid with increases from
        # the previous bid in the order of 1-3x the minimum bid. So, for
        # example, as the minimum bid is 8, then if any competitor bids more
        # than 24 than the previous value, then we know they can't be an NPC.

        # Maybe we want to bid somewhat like an NPC to disguise ourselves?

        pass

    def onMyTurn(self, lastBid):

        # This is where all our strategy for bidding comes in. This will most
        # likely be done probabilistically. Our priors are based off the
        # statistics and our posteriors are based off the other bots. This
        # reminds me of Figgie a lot.

        # If we know the true value, it's almost pointless for us to bid
        # straight to it. Although we would either win the item or not lose
        # points by overbidding and force other players to lose points for it,
        # we don't get any information on competitors. By my assessment, I think
        # the majority of the points are actually in determining and classifying
        # the other bots.

        pass

    def onAuctionEnd(self):

        # Here we report on the three categories for competitor bots.

        # Because the index or IDs of bots doesn't change between auctions, we
        # can carry over information from previous rounds to inform our guesses
        # in future rounds. For example, if we're extremely confident in
        # identifying one of our own bots from the first round, then we just
        # make the same report for all future rounds.
        pass