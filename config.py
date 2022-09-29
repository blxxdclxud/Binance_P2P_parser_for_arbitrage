import logging
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='binance.log')
logger = logging.getLogger(__name__)
