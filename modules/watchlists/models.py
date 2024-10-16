class Watchlist(Base):
    __tablename__ = "watchlists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    user = relationship("User", back_populates="watchlists")
    wallets_association = relationship("WatchlistWallets", back_populates="watchlist")
    coins_association = relationship("WatchlistCoins", back_populates="watchlist")
    pools_association = relationship("WatchlistPools", back_populates="watchlist")

    # For easy access to associated wallets, coins, and pools:
    wallets = relationship("Wallet", secondary="watchlist_wallets", viewonly=True)
    coins = relationship("Coin", secondary="watchlist_coins", viewonly=True)
    pools = relationship("Pool", secondary="watchlist_pools", viewonly=True)
