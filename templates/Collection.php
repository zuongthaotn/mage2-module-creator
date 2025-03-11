<?php
namespace {{namespace}}\{{module_name}}\Model\ResourceModel\{{interface_name}};

use {{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface;
use \Magento\Framework\Model\ResourceModel\Db\Collection\AbstractCollection;

/**
 * {{interface_name}} Collection
 */
class Collection extends AbstractCollection
{
    /**
     * @var string
     */
    protected $_idFieldName = '{{interface_name_lower}}_id';

    /**
     * @var string
     */
    protected $_eventPrefix = '{{interface_name_lower}}_collection_prevent';

    /**
     * @var string
     */
    protected $_eventObject = '{{interface_name_lower}}_collection';

    /**
     * Define resource model
     *
     * @return void
     */
    protected function _construct()
    {
        $this->_init(\{{namespace}}\{{module_name}}\Model\{{interface_name}}::class, \{{namespace}}\{{module_name}}\Model\ResourceModel\{{interface_name}}::class);
        $this->_map['fields']['{{interface_name_lower}}_id'] = 'main_table.{{interface_name_lower}}_id';
    }

    /**
     * Returns pairs {{interface_name_lower}}_id - name
     *
     * @return array
     */
    public function toOptionArray()
    {
        return $this->_toOptionArray('{{interface_name_lower}}_id', 'name');
    }
}
