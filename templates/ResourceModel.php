<?php
namespace {{namespace}}\{{module_name}}\Model\ResourceModel;

use {{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface;
use Magento\Framework\DB\Select;
use Magento\Framework\EntityManager\EntityManager;
use Magento\Framework\EntityManager\MetadataPool;
use Magento\Framework\Exception\LocalizedException;
use Magento\Framework\Model\AbstractModel;
use Magento\Framework\Model\ResourceModel\Db\AbstractDb;
use Magento\Framework\Model\ResourceModel\Db\Context;
use Magento\Store\Model\Store;
use Magento\Store\Model\StoreManagerInterface;

/**
 * {{interface_name_lower}} model
 * @SuppressWarnings(PHPMD.CouplingBetweenObjects)
 */
class {{interface_name}} extends AbstractDb
{

    /**
     * Initialize resource model
     *
     * @return void
     */
    protected function _construct()
    {
        $this->_init('{{interface_name_lower}}', '{{interface_name_lower}}_id');
    }
}
